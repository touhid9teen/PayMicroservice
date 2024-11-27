from django.contrib.auth.hashers import check_password, make_password
from rest_framework import serializers
from .models import AuthUser

class AuthRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ['username', 'email', 'user_number', 'current_balance', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True,
            }
        }





# class AuthLoginSerializer(serializers.Serializer):
#     email = serializers.EmailField(required=True)
#     password = serializers.CharField(write_only=True, required=True)
#
#     def validate(self, attrs):





