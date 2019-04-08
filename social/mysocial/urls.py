from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.com_list, name='com_list'),
    path('feed/', views.com_list, name='com_list'),
    path('feed/post/<int:pk>/', views.com_detail, name='com_detail'),
    path('feed/post/new/', views.com_new, name='com_new'),
    path('feed/post/<int:pk>/edit/', views.com_edit, name='com_edit'),
    # path('friend_list/', views.change_friends, name='friend_list'),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/<int:pk>/', views.view_profile, name='view_profile_with_pk'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('change-password/', views.change_password, name='change_password'),


]

# urlpatterns += [
#
#     url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_friends, name='change_friends')
# ]