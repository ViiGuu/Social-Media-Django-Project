from .  import views
from django.urls import path

app_name = 'posts_app'

urlpatterns = [
    path('', views.all_posts, name='all_posts'),
    path('/<slug:slug>', views.post_page, name = "page")
    ]
