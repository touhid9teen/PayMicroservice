from django.contrib import admin

from scheduler.models import Scheduler

# Register your models here.
admin.site.register(Scheduler)

from django_celery_beat.models import PeriodicTask, IntervalSchedule
