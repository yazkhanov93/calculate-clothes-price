from django.db import models
from django.contrib.auth.models import User

from store.models import ClothingItem, Size, Fabric, AdditionalService


class OrderStatus(models.Model):
    name = models.CharField(max_length=20, verbose_name="Status Name")
    
    class Meta:
        verbose_name_plural = "Order Status"
        
    def __str__(self):
        return self.name


class UserOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User", related_name="user_order")
    order_status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE, verbose_name="Order Status")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total Price")
    created_date = models.DateField(auto_now_add=True, verbose_name="Date of Create")
    updated_date = models.DateField(auto_now=True, verbose_name="Date of Update")
    
    class Meta:
        verbose_name_plural = "User Orders"
        
    def __str__(self):
        return str(self.user.username)
    

class OrderItem(models.Model):
    order = models.ForeignKey(UserOrder, on_delete=models.CASCADE, verbose_name="Order ID", related_name="order_item")
    clothes = models.ForeignKey(ClothingItem, on_delete=models.CASCADE, verbose_name="Clothes")
    size = models.ForeignKey(Size, on_delete=models.CASCADE, verbose_name="Size")
    fabric = models.ForeignKey(Fabric, on_delete=models.CASCADE, verbose_name="Fabric")
    add_service = models.ManyToManyField(AdditionalService, verbose_name="Additional Service")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    
    
    class Meta:
        verbose_name_plural = "Order Items"
    
    def __str__(self):
        return str(self.order.id)
    