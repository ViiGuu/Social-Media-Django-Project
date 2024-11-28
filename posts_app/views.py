from django.shortcuts import render
from main.models import Post, Comment
from profile_app.models import Profile
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def all_posts(request):
    posts = Post.objects.all()
    num_comments = [len(Comment.objects.filter(post_id=post.id)) for post in posts]
    user_images = list(Profile.objects.values_list('profile_pic', flat=True))
    print(user_images[0])
    profile = Profile.objects.get(user=request.user)
    return render(request, 'posts_app/all_posts.html', {'posts': posts, 'num_comments': num_comments, 'user_images': user_images,  'profile': profile})


@login_required
def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    comments = Comment.objects.filter(post_id=post.id)
    profile = Profile.objects.get(user=request.user)
    
    if request.method == 'POST':
        body = request.POST.get('body')
        new_comment = Comment.objects.get_or_create(post = post, author = request.user, body=body)[0]
        new_comment.save()            
    return render(request, 'posts_app/post_page.html', {'post':post, 'post_id': post.id, 'comments': comments, 'profile': profile})


@login_required
def my_posts(request):
    user = request.user
    posts = user.posts.all()
    return render(request, 'posts_app/my_posts.html', {'posts':posts})


@login_required
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    user = request.user
    posts = user.posts.all()
    return render(request, 'posts_app/my_posts.html', {'posts':posts})