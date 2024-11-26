from django.shortcuts import render
from main.models import Post, Comment

# Create your views here.
def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    comments = Comment.objects.filter(post_id=post.id)
    
    if request.method == 'POST':
        body = request.POST.get('body')
        new_comment = Comment.objects.get_or_create(post = post, author = request.user, body=body)[0]
        new_comment.save()            
    return render(request, 'posts_app/post_page.html', {'post':post, 'post_id': post.id, 'comments': comments})


#Yamit:
def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'posts_app/yamit_posts_list.html', {'posts': posts})

