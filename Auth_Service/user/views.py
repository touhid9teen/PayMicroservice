from requests import Response
from rest_framework.views import APIView
from .models import AuthUser
from .serializers import AuthRegisterSerializer
from rest_framework.response import Response
from rest_framework import status
from .utils import token_generator, refresh_token_generator


class AuthRegisterView(APIView):
    def post(self, request):
        serializer = AuthRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthLoginView(APIView):
    def post(self, request):

        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = AuthUser.objects.get(email=email)

            if user is None:
                return Response({"message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)

            access_token = token_generator(user)
            refresh_token = refresh_token_generator(user)

            return Response({
                "access_token": str(access_token),
                "refresh_token": str(refresh_token)
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)