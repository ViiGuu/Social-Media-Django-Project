from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()    
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField( upload_to='photos/',blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None)
    author = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)