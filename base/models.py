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


     def __str__(self):
        return str(self.user)
    
     def num_image(self):
        return self.profile.all().count()
    
    
        
     def save_profile(self):
        self.save()

     def delete_profile(self):
        self.delete()

     def update(self, profilePhoto, bio):
        self.bio = bio
        self.profilePhoto = profilePhoto
        self.save()


class Project(models.Model):
    image = CloudinaryField('image')
    title = models.CharField(max_length=20)
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user',null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile',null=True)

    @classmethod
    def search_by_title(cls,search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects

    class Meta:
        ordering = ['-updated','-created']
    
    def __str__(self):
        return self.name 
    
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_description(self, description, name):
        self.caption = description
        self.name = name
        self.save()