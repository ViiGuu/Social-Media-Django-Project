from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_pic = models.ImageField(default = 'profile_images/user.png', upload_to='profile_images/',blank=True, null=True)
    gender = models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)
    age = models.IntegerField(default=None)

    @property
    def profile_pic_url(self):
        if self.profile_pic:
            return self.profile_pic.url
        else:
            return f'{settings.MEDIA_URL}profile_images/user.png'
            

    def __str__(self):
        return f"{self.user.username}'s Profile"
