from rest_framework import serializers
from django.contrib.auth.models import User

from order.models import *
from store.models import *

from api.clothes.serializers import *


class OrderSerializerList(serializers.ModelSerializer):
    class Meta:
        model = UserOrder
        fields = "__all__"
        
        
class OrderItemSerialer(serializers.ModelSerializer):
    size = SizeSerializer()
    fabric = FabricSerializer()
    add_service = AdditionalServiceSerializer(many=True, read_only=True)
    clothes = ClothingItemSerializer()
    class Meta:
        model = OrderItem
        fields = ["id", "order", "clothes", "price", "fabric", "add_service", "size"]


class CreateOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"