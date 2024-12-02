# from rest_framework import serializers
# from .models import MoneyTransfer
#
# class MoneyTransferRequestSerializer(serializers.Serializer):
#     amount = serializers.DecimalField(max_digits=12, decimal_places=2)
#     narration = serializers.CharField(max_length=500)
#     auto_pay = serializers.BooleanField(default=False)
#     payment_frequency = serializers.CharField(read_only=False, allow_blank=True, required=False)
#
#
from rest_framework import serializers
from .models import MoneyTransfer

class MoneyTransferRequestSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    narration = serializers.CharField(max_length=255)
    payment_frequency = serializers.ChoiceField(
        choices=['daily', 'weekly', 'monthly', 'yearly'],
        required=False
    )
    auto_pay = serializers.BooleanField(default=False)
