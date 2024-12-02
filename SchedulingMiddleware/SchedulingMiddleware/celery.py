from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scheduler_service.settings')

app = Celery('scheduler_service')

# Read settings from Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Autodiscover tasks
app.autodiscover_tasks()
