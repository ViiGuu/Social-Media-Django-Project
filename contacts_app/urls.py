from django.urls import path
from . import views

app_name = 'contacts_app'

urlpatterns = [
    path('show_profile/<int:id>', views.show_profile, name='show_profile'),
    path('friends', views.friends, name='friends'),
    path('send_request/<int:user_id>/', views.send_request, name='send_request'),
    path('accept_request/<int:request_id>/', views.accept_request_view, name='accept_request'),
    path('reject_request/<int:request_id>/', views.reject_request_view, name='reject_request'),
]
