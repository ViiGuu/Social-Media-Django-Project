from .views import *
from django.urls import path

app_name = 'users'

urlpatterns = [
    path('', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('logout/', user_logout, name='logout')
]