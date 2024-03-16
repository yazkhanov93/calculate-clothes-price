from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="User")
    name = models.CharField(max_length=100, verbose_name="Full Name", blank=True, null=True)
    contacts = models.CharField(max_length=255, verbose_name="Contacts", blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "User Profiles"
        
    def __str__(self):
        return self.name