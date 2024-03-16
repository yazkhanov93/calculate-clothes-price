from django.contrib import admin
from .models import *


@admin.register(OrderStatus)
class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ["name"]


class OrderItemAdmin(admin.StackedInline):
    model = OrderItem
    extra = 0
    
    
@admin.register(UserOrder)
class UserOrderAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "order_status", "total_price", "created_date", "updated_date"]
    search_fields = ["order_status", "total_price"]
    list_filter = ["order_status", "created_date", "updated_date"]
    list_editable = ["order_status"]
    inlines = [OrderItemAdmin]
    