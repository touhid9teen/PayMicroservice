from rest_framework import serializers
from .models import Service

class ServiceVerifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['service_user_name', 'password']

    def validate(self, attrs):
        service_user_name = attrs.get('service_user_name')
        password = attrs.get('password')

        # Ensure all required fields are provided
        if not service_user_name or not password:
            raise serializers.ValidationError({
                'error': 'All fields (id, service_user_name, and password) are required.'
            })

        service = Service.objects.filter(service_user_name=service_user_name, password=password).first()
        if not service:
            raise serializers.ValidationError({'error': 'Service with the provided credentials does not exist.'})



        # Activate the service
        service.is_active = True
        service.save()
        return attrs

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['service_user_name', 'password']



