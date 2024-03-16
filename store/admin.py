from django.contrib import admin
from .models import *


@admin.register(ClothingItem)
class ClothingItemAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    search_fields = ["name"]


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ["size", "price"]
    search_fields = ["size", "price"]
    list_filter = ["size", "price"]
    

@admin.register(Fabric)
class FabricAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]
    search_fields = ["name", "price"]
    list_filter = ["name", "price"]
    
    
@admin.register(AdditionalService)
class AdditionalServiceAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]
    search_fields = ["name", "price"]
    list_filter = ["name", "price"]

