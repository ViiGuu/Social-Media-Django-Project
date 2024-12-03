from .models import FriendshipRequest, Friendship
from django.contrib.auth.models import User

def send_friend_request(from_user, to_user):
    if from_user != to_user:
        request, created = FriendshipRequest.objects.get_or_create(from_user=from_user, to_user=to_user)
        if created:
            return f"Request for friendship sent {to_user.username}."
        else:
            return f"Request allready sent to {to_user.username}."

def accept_friend_request(request_id):
    friend_request = FriendshipRequest.objects.get(id=request_id)
    if friend_request.status == 'pending':
        friend_request.accept()
        return f"Accepted friend request from {friend_request.from_user.username}."
    return "Request already processed."

def reject_friend_request(request_id):
    friend_request = FriendshipRequest.objects.get(id=request_id)
    if friend_request.status == 'pending':
        friend_request.reject()
        return f"You rejected friend request from {friend_request.from_user.username}."
    elif friend_request.status == 'accepted':
        friend_request.reject()
        
    return "Request already processed."

def get_friends(user):
    friendships = Friendship.objects.filter(user1=user).values_list('user2', flat=True) | \
                  Friendship.objects.filter(user2=user).values_list('user1', flat=True)
    return User.objects.filter(id__in=friendships)
