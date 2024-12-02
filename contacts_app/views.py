from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .services import send_friend_request, accept_friend_request, reject_friend_request
from django.contrib.auth.models import User
from main.models import Post
from profile_app.models import Profile
from .services import get_friends
from .models import Friendship, FriendshipRequest
from django.db.models import Q

# Create your views here.

@login_required
def show_friends(request):
    user = request.user
    friends = user.profile.friends
    received_friend_requests = user.received_friend_requests.all()
    return render(request, 'contacts_app/friends.html', {'friends': friends, 'received_friend_requests':received_friend_requests})

@login_required
def show_profile(request, id):
    user = User.objects.get(id=id)
    is_friend = FriendshipRequest.are_friends(request.user, user)
    if request.user == user:
        return redirect('profile_app:profile')
    friendship_status = FriendshipRequest.friendship_status(request.user, user)
    
    print(friendship_status)
    profile = user.profile
    return render(request, 'contacts_app/show_profile.html', {'profile': profile, 'friendship_status':friendship_status, 'is_friend': is_friend})

@login_required
def send_request(request, user_id):
    to_user = User.objects.get(id=user_id)
    profile = to_user.profile
    to_user = get_object_or_404(User, id=user_id)
    message = send_friend_request(request.user, to_user)
    friendship_status = FriendshipRequest.friendship_status(request.user, to_user)
    return render(request, 'contacts_app/show_profile.html', {'profile': profile, 'friendship_status': friendship_status})  

@login_required
def accept_request_view(request, request_id):
    message = accept_friend_request(request_id)
    messages.info(request, message)
    return redirect('contacts_app:show_friends')

@login_required
def reject_request_view(request, request_id):
    message = reject_friend_request(request_id)
    messages.info(request, message)
    return redirect('profile_page')


def cancel_friend_request(request, to_user_id):
    to_user = User.objects.get(id=to_user_id)
    profile = to_user.profile
    

    try:
        to_user = User.objects.get(id=to_user_id)
        friend_request = FriendshipRequest.objects.get(from_user=request.user, to_user=to_user, status='pending')
        friend_request.delete()
        friendship_status = FriendshipRequest.friendship_status(request.user, to_user)

        return render(request, 'contacts_app/show_profile.html', {'profile': profile, 'friendship_status': friendship_status})  
    
    except FriendshipRequest.DoesNotExist:
        return HttpResponse("The friend request was not found or has already been accepted/rejected.")


def remove_friend(request, friend_id):
    
    try:
        # Get the user who needs to be removed from friends
        friend_to_remove = User.objects.get(id=friend_id)
        # Find the friendship record between the current user and the selected user
        friendship = Friendship.objects.get(
            Q(user1=request.user, user2=friend_to_remove) | Q(user1=friend_to_remove, user2=request.user)
        )
        
        # Delete the friendship record
        friendship.delete()
        FriendshipRequest.delete_all_friendship_requests(request.user, friend_to_remove)

        return redirect('contacts_app:show_profile', id=friend_id)
    
    except Friendship.DoesNotExist:
        return HttpResponse("Friendship record not found.")

