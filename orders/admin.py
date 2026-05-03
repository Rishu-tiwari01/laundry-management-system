from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'customer_name', 'phone', 'garment', 'total_bill', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['order_id', 'customer_name', 'phone']
    readonly_fields = ['order_id', 'total_bill', 'created_at']
