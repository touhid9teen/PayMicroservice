from django.contrib import admin
from .models import MoneyTransfer
# Register your models here.


@admin.register(MoneyTransfer)
class MoneyTransferAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'user_number',
        'amount',
        'status',
        'created_at',
        'narration',
    )

    date_hierarchy = 'created_at'