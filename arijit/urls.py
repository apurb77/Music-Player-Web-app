from django.contrib import admin
from django.urls import include, path

app_name = 'arijit'

from arijit import views
urlpatterns = [
     path('', views.main, name='main'),
]