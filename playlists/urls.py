from django.contrib import admin
from django.urls import include, path

app_name = 'playlists'

from playlists import views
urlpatterns = [
     path('', views.home, name='home'),
     path('<int:id>', views.songpost, name='songpost')
]