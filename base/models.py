from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE)
     profilePhoto = CloudinaryField('image')
     bio = models.TextField(max_length=200, blank=True)
     updated = models.DateTimeField(auto_now=True)
     created = models.DateTimeField(auto_now_add=True)