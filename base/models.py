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

class Project(models.Model):
    image = CloudinaryField('image')
    title = models.CharField(max_length=20)
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user',null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile',null=True)