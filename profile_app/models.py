from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_pic = models.ImageField(default = 'profile_img.jpg', upload_to='photos/',blank=True, null=True)
    # gender = models.CharField(default=None, max_length=1) # Need to add on registration or blank=True
    # age = models.IntegerField(default=None)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"