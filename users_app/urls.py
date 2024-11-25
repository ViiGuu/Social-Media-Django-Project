from .views import *
from django.urls import path

app_name = 'users'

urlpatterns = [
    path('register/', register, name='register')
]