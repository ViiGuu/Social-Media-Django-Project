from .  import views
from django.urls import path

app_name = 'posts_app'

urlpatterns = [
    path('all_posts/', views.all_posts, name='all_posts'),
    path('all_posts/<slug:slug>', views.post_page, name = "page")
    #path('all_posts/', views.posts_list, name = "list")
    ]
