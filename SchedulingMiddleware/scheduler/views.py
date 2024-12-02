from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from scheduler.authenticate import CustomAuthentication
from .serializers import SchedulerSerializer
from .tasks import trigger_auto_payment

class SchedulerView(APIView):
    authentication_classes = [CustomAuthentication]
    serializer_class = SchedulerSerializer

    def post(self, request):
        """
        Create a schedule and trigger auto-payment task if necessary.
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            schedule = serializer.save()  # Save the schedule in the database

            # Trigger the Celery task for auto-payment
            if schedule.is_active:  # Check if the schedule is active
                trigger_auto_payment.delay(schedule.id)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
