from django.urls import path
from .views import TransferMoneyAPIView

urlpatterns = [
    path('', TransferMoneyAPIView.as_view(), name='transfer-money'),
]