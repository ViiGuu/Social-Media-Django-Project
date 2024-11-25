from .views import *
from django.urls import path
from django.contrib import admin
#from django.conf import settings
#from django.conf.urls.static import static

app_name = 'profile_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/',views.profile_view, name='profile'),
        
]

#if settings.DEBUG:
 #   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)