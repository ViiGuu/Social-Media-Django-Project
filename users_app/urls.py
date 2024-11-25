from .views import *
from django.urls import path

app_name = 'users'

urlpatterns = [
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login')
]