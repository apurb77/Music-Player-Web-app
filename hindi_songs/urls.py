from django.contrib import admin
from django.urls import include, path

app_name = 'songs'

from hindi_songs import views
urlpatterns = [
     path('', views.hindi, name='hindi'),
     
]