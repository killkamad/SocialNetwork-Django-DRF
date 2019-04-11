from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.com_list, name='com_list'),
    path('feed/', views.com_list, name='com_list'),
    path('feed/post/<int:pk>/', views.com_detail, name='com_detail'),
    path('feed/post/new/', views.com_new, name='com_new'),
    path('feed/post/<int:pk>/edit/', views.com_edit, name='com_edit'),
    # path('friend_list/', views.list_friends, name='friend_list'),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/<int:pk>/', views.view_profile, name='view_profile_with_pk'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('change-password/', views.change_password, name='change_password'),


]

# urlpatterns += [
#
#     url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_friends, name='change_friends')
# ]

# urlpatterns+= [
#     url(r'^$', views.users_list, name='list'),
#     url(r'^(?P<slug>[\w-]+)/$', views.profile_view),
#     url(r'^friend-request/send/(?P<id>[\w-]+)/$', views.send_friend_request),
#     url(r'^friend-request/cancel/(?P<id>[\w-]+)/$', views.cancel_friend_request),
#     url(r'^friend-request/accept/(?P<id>[\w-]+)/$', views.accept_friend_request),
#     url(r'^friend-request/delete/(?P<id>[\w-]+)/$', views.delete_friend_request),
# ]