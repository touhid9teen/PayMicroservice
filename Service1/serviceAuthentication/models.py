from django.db import models

class Service(models.Model):
    service_name = models.CharField(max_length=50)
    service_user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)