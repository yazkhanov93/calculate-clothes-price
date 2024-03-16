from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="User")
    name = models.CharField(max_length=100, verbose_name="Full Name", blank=True, null=True)
    contacts = models.CharField(max_length=255, verbose_name="Contacts", blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "User Profiles"
        
    def __str__(self):
        return str(self.name)
    
    @receiver(post_save, sender=User)
    def create_user_info(sender, instance, created, **kwargs):
        if created:
            staff = Profile(user=instance)
            staff.save()