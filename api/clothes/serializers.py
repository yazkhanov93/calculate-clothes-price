from rest_framework import serializers
from store.models import ClothingItem, Size, Fabric, AdditionalService


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ["id", "size", "price"]
        

class FabricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fabric
        fields = ["id", "name", "image", "description", "price"]


class AdditionalServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalService
        fields = ["id", "name", "description", "price"]


class ClothingItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothingItem
        fields = "__all__"
        
        
class ClothingItemDetailSerializer(serializers.ModelSerializer):
    size = serializers.SerializerMethodField()
    fabric = serializers.SerializerMethodField()
    add_service = serializers.SerializerMethodField()
    class Meta:
        model = ClothingItem
        fields = ["name", "image", "description", "size", "fabric", "add_service"]
        
    def get_size(self, obj):
        try:
            size = Size.objects.filter(clothes=obj)
            return SizeSerializer(size, many=True).data
        except:
            pass
        
    def get_fabric(self, obj):
        try:
            fabric = Fabric.objects.filter(clothes=obj)
            return FabricSerializer(fabric, many=True).data
        except:
            pass
    
    def get_add_service(self, obj):
        try:
            add_service = AdditionalService.objects.filter(clothes=obj)
            return AdditionalServiceSerializer(add_service, many=True).data
        except:
            pass