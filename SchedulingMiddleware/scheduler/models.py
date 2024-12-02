from django.db import models
from django.utils.timezone import now

class Scheduler(models.Model):
    username = models.CharField(max_length=255)
    user_number = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    narration = models.TextField()
    service_url = models.URLField()
    payment_frequency = models.CharField(
        max_length=50,
        choices=[
            ('daily', 'Daily'),
            ('weekly', 'Weekly'),
            ('monthly', 'Monthly'),
            ('yearly', 'Yearly'),
        ]
    )
    next_payment_date = models.DateTimeField(default=now)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
