from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q

# Create your models here.

class Friendship(models.Model):
    user1 = models.ForeignKey(User, related_name='friendships_as_user1', on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, related_name='friendships_as_user2', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Meta:
        unique_together = ('user1', 'user2')

def __str__(self):
    return f"{self.user1.username} - {self.user2.username}"



class FriendshipRequest(models.Model):
    from_user = models.ForeignKey(User, related_name='sent_friend_requests', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='received_friend_requests', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')],
        default='pending',
        max_length=10
    )

    class Meta:
        unique_together = ('from_user', 'to_user')

    
    def accept(self):
        self.status = 'accepted'
        self.save()
        Friendship.objects.create(user1=self.from_user, user2=self.to_user)

    def reject(self):
        self.status = 'rejected'
        self.save()

    def __str__(self):
        return f"{self.from_user.username} -> {self.to_user.username} ({self.status})"
    
    @staticmethod
    def are_friends(user1, user2):
        return Friendship.objects.filter(
            (Q(user1=user1) & Q(user2=user2)) | 
            (Q(user1=user2) & Q(user2=user1))
        ).exists()
    
    
    def friendship_status(user1, user2):
        try:
            friend_request = FriendshipRequest.objects.get(
                Q(from_user=user1, to_user=user2) | Q(from_user=user2, to_user=user1)
            )
            return friend_request.status
        except FriendshipRequest.DoesNotExist:
            return None
        
    def delete_all_friendship_requests(user1, user2):
        FriendshipRequest.objects.filter(
            (Q(from_user=user1) & Q(to_user=user2)) |
            (Q(from_user=user2) & Q(to_user=user1))
        ).delete()

    
