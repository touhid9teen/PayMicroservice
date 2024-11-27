from django.urls import path
from .views import ServiceVerifyView, GetTokenView

urlpatterns = [
    path('verify/', ServiceVerifyView.as_view(), name='login'),
    path('get-token/', GetTokenView.as_view(), name='register'),
]