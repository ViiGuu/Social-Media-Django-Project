from django.urls import path
from . import views

app_name = 'profile_app'

urlpatterns = [
    path('',views.profile_view, name='profile'),
    path('update/',views.update_profile, name='update_profile')
]
