from .  import views
from django.urls import path

app_name = 'posts_app'

urlpatterns = [
    path('all_posts/', views.all_posts, name='all_posts'),
    path('all_posts/<slug:slug>', views.post_page, name = "page"),
    path('my_posts', views.my_posts, name = 'my_posts'),
    path('my_posts/<int:post_id>', views.delete_post, name = 'delete_post'),
    ]
