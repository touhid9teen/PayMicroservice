from django.db import models

class Scheduler(models.Model):

    username = models.CharField(max_length=50)
    user_number = models.CharField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_frequency = models.CharField()
    narration = models.TextField()
    service_name = models.TextField()
    service_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.username