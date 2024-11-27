from django.core.serializers import serialize
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from transferMoneyService import settings
from .models import MoneyTransfer, Status
from .serializers import MoneyTransferRequestSerializer
from .authenticate import CustomAuthentication
import requests
import json
from transferMoneyService.settings import SERVICE_AUTH_TOKEN_URL, SERVICE_USER_NAME, SERVICE_PASSWORD, SCHEDULE_SERVICE_URL



class TransferMoneyAPIView(APIView):
    authentication_classes = [CustomAuthentication]
    serializer_class = MoneyTransferRequestSerializer
    request = None
    money_transfer_serializer = None

    # def __init__(self):
    #     super().__init__(TransferMoneyAPIView)

    def create_schedule(self):
        payload = {
            "service_user_name": SERVICE_USER_NAME,
            "password": SERVICE_PASSWORD
        }

        token_response = requests.post(url=SERVICE_AUTH_TOKEN_URL, json=payload)

        if not status.is_success(token_response.status_code):
            print(f"Error: {token_response.status_code}, Response: {token_response.text}")
            return False


        schedule_service_url = settings.SCHEDULE_SERVICE_URL
        request_payload = {
            'amount' : float(self.money_transfer_serializer.validated_data['amount']),
            'username' : self.request.user.username,
            'user_number' : self.request.user.user_number,
            'payment_frequency' :self.money_transfer_serializer.validated_data['payment_frequency'],
            'narration' : self.money_transfer_serializer.validated_data['narration'],
            'service_name' : settings.SERVICE_USER_NAME,
            'service_url' : settings.TRANSACTION_SCHEDULING_URL,
            'created_at' : self.money_transfer_serializer.validated_data['created_at'],
            'updated_at' : self.money_transfer_serializer.validated_data['updated_at'],
        }

        headers = {
            'Authorization': f"Bearer {token_response.json()['access_token']}"
        }
        
        try:
            response = requests.post(url=schedule_service_url, json=request_payload, headers=headers)
            if not status.is_success(response.status_code):
                return False
            return True
        except Exception as e:
            print(f"Error: {repr(e)}")



    def post(self, request):
        self.request = request
        transfer_money_data = {
            **request.data,
            'username': request.user.username,
            'user_number': request.user.user_number,
        }

        self.money_transfer_serializer = self.serializer_class(data=transfer_money_data)

        if not self.money_transfer_serializer.is_valid():
            return Response(data={"msg":"Transaction is not successful. Data error."},status=status.HTTP_400_BAD_REQUEST)



        money_transfer_data = MoneyTransfer.objects.create_transaction({
            'amount' : self.money_transfer_serializer.validated_data['amount'],
            'narration' : self.money_transfer_serializer.validated_data['narration'],
            'username' : request.user.username,
             'user_number' : request.user.user_number}
        )


        money_transfer_data.status = Status.SUCCESS
        money_transfer_data.save()

        current_balance = float(float(request.user.current_balance) - float(money_transfer_data.amount))
        if not self.money_transfer_serializer.validated_data['auto_pay']:
            return Response({"msg":"Transaction is successful.", "current_balance" : current_balance},status.HTTP_201_CREATED)

        if not self.create_schedule():
            return Response({"msg":"Transaction is successful. Auto pay not enable", "current_balance" : current_balance},status.HTTP_201_CREATED)

        return Response({"msg":"Transaction is successful. Auto pay enable", "current_balance" : current_balance},status.HTTP_201_CREATED)




