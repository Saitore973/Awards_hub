from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def customer_profile(sender, instance, created,**kwargs):
    if created:
        Profile.objects.create(user=instance, name=instance.username)

# post_save.connect(customer_profile, sender=User)
 
    