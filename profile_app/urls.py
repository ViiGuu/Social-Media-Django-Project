from django.urls import path
from . import views

app_name = 'profile_app'

urlpatterns = [
    path('my_profile/',views.profile_view, name='profile'),
]
