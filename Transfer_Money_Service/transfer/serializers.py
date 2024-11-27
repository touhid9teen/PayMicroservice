from rest_framework import serializers
from .models import MoneyTransfer

class MoneyTransferRequestSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=12, decimal_places=2)
    narration = serializers.CharField(max_length=500)
    auto_pay = serializers.BooleanField(default=False)
    payment_frequency = serializers.CharField(read_only=False, allow_blank=True, required=False)


