from django.core.serializers import serialize
from requests import Response
from rest_framework.views import APIView
from .models import Service
from .serializers import ServiceVerifySerializer, ServiceSerializer
from rest_framework.response import Response
from rest_framework import status
from .utils import token_generator, refresh_token_generator


class ServiceVerifyView(APIView):
    def post(self, request):
        serializer = ServiceVerifySerializer(data=request.data)
        if(not serializer.is_valid()):
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            service = Service.objects.filter(service_user_name=serializer.data['service_user_name'], password=serializer.data['password'],).first()
            access_token = token_generator(service)
            refresh_token = refresh_token_generator(service)
            return Response({'access_token' : access_token, 'refresh_token' : refresh_token}, status=status.HTTP_200_OK)
        except Service.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error' : str(e)}, status=status.HTTP_400_BAD_REQUEST)


class GetTokenView(APIView):
    def post(self, request):
        serializer = ServiceSerializer(data=request.data)
        if(not serializer.is_valid()):
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            service = Service.objects.filter(service_user_name=serializer.data['service_user_name'], password=serializer.data['password'],).first()
            access_token = token_generator(service)
            refresh_token = refresh_token_generator(service)
            return Response({'access_token' : access_token, 'refresh_token' : refresh_token}, status=status.HTTP_200_OK)
        except Service.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error' : str(e)}, status=status.HTTP_400_BAD_REQUEST)
