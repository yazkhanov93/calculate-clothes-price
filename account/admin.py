from django.contrib import admin
from .models import *


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["name", "contacts"]
    search_fields = ["name", "contacts"]