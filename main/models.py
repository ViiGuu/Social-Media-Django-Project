from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()    
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default="post_images/christmas_gift.jpeg", upload_to='post_images/', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name='posts')

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date'] 

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return  self.author.username + "'s comment on " + self.post.title + " by " + self.post.author.username
