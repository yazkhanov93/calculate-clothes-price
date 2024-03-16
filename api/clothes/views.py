from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import permission_classes
from django.db.models import Q
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from store.models import *
from .serializers import *


class ClothingItemsView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            clothesItems = ClothingItem.objects.all()
            serializer = ClothingItemSerializer(clothesItems, many=True)
            return Response(serializer.data)
        except Exception as e:
            raise ParseError(e)
        

class ClothingItemDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        try:
            clothesItem = ClothingItem.objects.get(id=pk)
            serializer = ClothingItemDetailSerializer(clothesItem, many=False)
            return Response(serializer.data)
        except Exception as e:
            raise ParseError(e)