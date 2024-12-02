from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .services import send_friend_request, accept_friend_request, reject_friend_request
from django.contrib.auth.models import User
from main.models import Post
from profile_app.models import Profile


# Create your views here.

@login_required
def friends(request):
    posts = Post.objects.all()
    users = User.objects.all()
    return render(request, 'contacts_app/friends.html', {'users': users, 'posts': posts})

@login_required
def show_profile(request, id):
    user = User.objects.get(id=id)
    profile = user.profile
    return render(request, 'contacts_app/show_profile.html', {'profile': profile})

@login_required
def send_request(request, user_id):
    to_user = get_object_or_404(User, id=user_id)
    message = send_friend_request(request.user, to_user)
    # messages.info(request, message)
    return render('contacts_app/show_profile.html', {'message': message})  

@login_required
def accept_request_view(request, request_id):
    message = accept_friend_request(request_id)
    messages.info(request, message)
    return redirect('profile_page')

@login_required
def reject_request_view(request, request_id):
    message = reject_friend_request(request_id)
    messages.info(request, message)
    return redirect('profile_page')


