from django.urls import path
from . import views

app_name = 'profile_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('/',views.profile_view, name='profile'),
]
