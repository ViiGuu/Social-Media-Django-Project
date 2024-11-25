from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from profile_app.models import Profile

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()    
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
