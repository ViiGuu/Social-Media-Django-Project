from .  import views
from django.urls import path

app_name = 'posts_app'

urlpatterns = [
    path('', views.all_posts, name='all_posts'),
    path('my_post/<slug:slug>', views.post_page, name = "page"),
    path('my_posts', views.my_posts, name = 'my_posts'),
    path('my_posts/<int:post_id>', views.delete_post, name = 'delete_post'),
    path('new_post', views.new_post, name='new_post'),
    path('my_posts/update/<int:id>', views.update_post, name='update_post'),
    path('update_comment/<int:comment_id>/<slug:slug>', views.update_comment, name='update_comment'),
    path('posts_commented', views.posts_commented, name='posts_commented'),
    path('delete_comment/<int:comment_id>/<slug:slug>', views.delete_comment, name = 'delete_comment'),

    ]

