from django.contrib import admin
from .models import *


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user","name", "contacts"]
    search_fields = ["user", "name", "contacts"]