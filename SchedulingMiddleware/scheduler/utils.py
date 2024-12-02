import jwt
from rest_framework.exceptions import PermissionDenied
from SchedulingMiddleware.settings import SECRET_KEY
from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json


def decode_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        raise PermissionDenied('Token has expired')
    except jwt.InvalidTokenError:
        raise PermissionDenied('token is invalid')


def get_token_from_header(auth_header):
    parts = auth_header.split()
    if parts[0].lower() != 'bearer':
        raise PermissionDenied('Authorization header must start with Bearer')
    if len(parts) == 1:
        raise PermissionDenied('Token not provided')
    elif len(parts) > 2:
        raise PermissionDenied('Authorization header must be Bearer token')
    return parts[1]


def register_celery_beat_task(schedule_id, frequency):
    interval = None
    if frequency == 'daily':
        interval, _ = IntervalSchedule.objects.get_or_create(every=1, period=IntervalSchedule.DAYS)
    elif frequency == 'weekly':
        interval, _ = IntervalSchedule.objects.get_or_create(every=7, period=IntervalSchedule.DAYS)
    elif frequency == 'monthly':
        interval, _ = IntervalSchedule.objects.get_or_create(every=30, period=IntervalSchedule.DAYS)
    elif frequency == 'yearly':
        interval, _ = IntervalSchedule.objects.get_or_create(every=365, period=IntervalSchedule.DAYS)

    if interval:
        PeriodicTask.objects.create(
            interval=interval,
            name=f"Auto Payment Task for Schedule {schedule_id}",
            task="scheduler_service.tasks.trigger_auto_payment",
            args=json.dumps([schedule_id])
        )
