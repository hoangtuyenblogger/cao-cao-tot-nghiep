from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('news/', views.news, name = 'search_news'),
    path('post/', views.post, name = 'post'),
]
