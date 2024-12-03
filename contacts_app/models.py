from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q

# Create your models here.

class Friendship(models.Model):
    user1 = models.ForeignKey(User, related_name='friendships_as_user1', on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, related_name='friendships_as_user2', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
            constraints = [
                models.UniqueConstraint(
                    fields=['user1', 'user2'],
                    name='unique_friendship'
                )
            ]
    
    def __str__(self):
        return f"{self.user1.username} - {self.user2.username}"
    
    
    def save(self, *args, **kwargs):
        if self.user1.id > self.user2.id:
            self.user1, self.user2 = self.user2, self.user1
        super().save(*args, **kwargs)



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


    def __str__(self):
        return f"{self.from_user.username} -> {self.to_user.username} ({self.status})"
    

    

    
    def accept(self):
        # self.status = 'accepted'
        # self.save()
        friend_request = FriendshipRequest.objects.get(from_user=self.from_user, to_user=self.to_user)
        friend_request.delete()

        friendship = Friendship(user1=self.from_user, user2=self.to_user)
        friendship.save()


    def reject(self):
        # self.status = 'rejected'
        # self.save()
        friend_request = FriendshipRequest.objects.get(from_user=self.from_user, to_user=self.to_user)
        friend_request.delete()

    
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

    
