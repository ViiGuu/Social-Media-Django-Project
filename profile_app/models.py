from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_pic = models.ImageField(default = 'profile_images/user.png', upload_to='profile_images/',blank=True, null=True)
    gender = models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)
    age = models.IntegerField(default=None)

    def __str__(self):
        return f"{self.user.username}'s Profile"
