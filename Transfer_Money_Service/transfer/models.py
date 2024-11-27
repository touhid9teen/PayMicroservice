from multiprocessing.managers import BaseManager

from django.db import models


class MoneyTransferManager(models.Manager):
    def create_transaction(self, data: dict):
        return self.create(**data)


class Status(models.TextChoices):
    SUCCESS = "success", "Success"
    PENDING = "pending", "Pending"
    FAILED = "failed", "Failed"

class MoneyTransfer(models.Model):



    # PAYMENT_TYPES = (
    #     ('daily', 'Daily'),
    #     ('weekly', 'Weekly'),
    #     ('monthly', 'Monthly'),
    #     ('Yearly', 'Yearly'),
    # )


    username = models.CharField(max_length=50)
    user_number = models.CharField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    narration = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)

    objects = MoneyTransferManager()

    def __str__(self):
        return self.username