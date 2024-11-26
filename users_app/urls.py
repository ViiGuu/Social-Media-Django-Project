from .views import *
from django.urls import path

app_name = 'users'

urlpatterns = [
    path('', start_page, name='start_page'),
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
]