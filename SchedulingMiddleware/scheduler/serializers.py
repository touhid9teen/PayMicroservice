from rest_framework import serializers
from scheduler.models import Scheduler


class SchedulerSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    username = serializers.CharField()
    user_number = serializers.CharField()
    payment_frequency = serializers.CharField()
    narration = serializers.CharField()
    service_name = serializers.CharField()
    service_url = serializers.URLField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return  Scheduler.objects.create(**validated_data)

    def to_representation(self, instance):

        representation = super().to_representation(instance)

        if not hasattr(instance, 'created_at') or not hasattr(instance, 'updated_at'):
            raise AttributeError("Instance does not have the required attributes: 'created_at' or 'updated_at'.")

        return representation
