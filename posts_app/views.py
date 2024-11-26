from django.shortcuts import render
from main.models import Post

# Create your views here.
def all_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts_app/all_posts.html', {'posts': posts})
    