from django.db.models.signals import post_save
from django.dispatch import receiver
from .models Profile
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs) :
    if created :
        profile = Profile.objects.create(user=instance, email=instance.email)
        profile.save()