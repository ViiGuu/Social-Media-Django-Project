from .  import views
from django.urls import path

app_name = 'posts_app'

urlpatterns = [
    path('all_posts/', views.all_posts, name='all_posts'),
]