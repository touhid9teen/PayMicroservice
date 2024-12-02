from celery import shared_task
from .models import Scheduler
from django.utils.timezone import now
from datetime import timedelta
import requests

@shared_task
def trigger_auto_payment(schedule_id):
    try:
        schedule = Scheduler.objects.get(id=schedule_id, is_active=True)
        if now() >= schedule.next_payment_date:
            response = requests.post(schedule.service_url, json={
                "username": schedule.username,
                "user_number": schedule.user_number,
                "amount": str(schedule.amount),
                "narration": schedule.narration,
            })

            if response.status_code == 200:
                update_next_payment_date(schedule)
            else:
                print(f"Payment failed: {response.status_code} - {response.text}")
    except Scheduler.DoesNotExist:
        print(f"Scheduler ID {schedule_id} not found.")

def update_next_payment_date(schedule):
    if schedule.payment_frequency == 'daily':
        schedule.next_payment_date += timedelta(days=1)
    elif schedule.payment_frequency == 'weekly':
        schedule.next_payment_date += timedelta(weeks=1)
    elif schedule.payment_frequency == 'monthly':
        schedule.next_payment_date += timedelta(days=30)
    elif schedule.payment_frequency == 'yearly':
        schedule.next_payment_date += timedelta(days=365)
    schedule.save()
