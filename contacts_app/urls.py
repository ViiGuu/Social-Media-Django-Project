from django.urls import path
from . import views

app_name = 'contacts_app'

urlpatterns = [
    path('show_profile/<int:id>', views.show_profile, name='show_profile'),
    path('show_friends', views.show_friends, name='show_friends'),
    path('send_request/<int:user_id>/', views.send_request, name='send_request'),
    path('accept_request/<int:request_id>/', views.accept_request_view, name='accept_request'),
    path('reject_request/<int:request_id>/', views.reject_request_view, name='reject_request'),
    path('cancel_friend_request/<int:to_user_id>/', views.cancel_friend_request, name='cancel_friend_request'),
    path('remove_friend/<int:friend_id>/', views.remove_friend, name='remove_friend'),
]
