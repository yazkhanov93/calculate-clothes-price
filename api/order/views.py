from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import permission_classes
from django.db.models import Q
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from store.models import *
from order.models import *
from .serializers import *


class OrderListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            orders = UserOrder.objects.filter(user=request.user)
            serializer = OrderSerializerList(orders, many=True)
            return Response(serializer.data)
        except Exception as e:
            raise ParseError(e)
        

class OrderItemView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        try:
            order = OrderItem.objects.get(order__id=pk)
            serializer = OrderItemSerialer(order, many=False)
            return Response(serializer.data)
        except Exception as e:
            raise ParseError(e)
        

class CreateOrderView(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(request_body=CreateOrderItemSerializer)
    def post(self, request):
        try:
            data = request.data
            data["user"] = request.user.id
            total_price = data["total_price"]
            serializer = OrderSerializerList(data=data)
            if serializer.is_valid():
                serializer.save()
                for item in data["items"]:
                    item["order"] = serializer.data["id"]
                    clothes = ClothingItem.objects.get(id=item["clothes"])
                    item["clothes"] = clothes.id
                    item_serializer = CreateOrderItemSerializer(data=item)
                    if item_serializer.is_valid():
                        item_serializer.save()
            return Response(item_serializer.data) 
        except Exception as e:
            raise ParseError(e)