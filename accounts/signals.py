from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser
from social.models import UserSocialProfile


@receiver(post_save, sender=CustomUser)
def create_user_social_profile(sender, instance, created, **kwargs):
    if created:
        UserSocialProfile.objects.create(owner=instance)