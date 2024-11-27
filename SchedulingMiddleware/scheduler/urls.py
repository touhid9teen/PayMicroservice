from django.urls import path
from .views import SchedulerView

urlpatterns = [
    path('create/', SchedulerView.as_view(), name='scheduler'),
]