from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.com_list, name='com_list'),\
    path('Feed/', views.com_list, name='com_list'),
    path('feed/post/<int:pk>/', views.com_detail, name='com_detail'),
    path('feed/post/new/', views.com_new, name='com_new'),
    path('feed/post/<int:pk>/edit/', views.com_edit, name='com_edit'),


]