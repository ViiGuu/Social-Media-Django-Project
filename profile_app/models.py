from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_pic = models.ImageField( upload_to='photos/',blank=True, null=True,default="default.jpg")
    created_at = models.DateField(default=datetime.date.today)
    updated_at = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f"{self.user.username}'s Profile"