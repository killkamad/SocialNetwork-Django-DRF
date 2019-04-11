from django.conf.urls import url
from django.urls import path
from . import views


# urlpatterns = [
#     url(r'^$', views.users_list, name='list'),
#     url(r'^(?P<slug>[\w-]+)/$', views.profile_view),
#     url(r'^friend-request/send/(?P<id>[\w-]+)/$', views.send_friend_request),
#     url(r'^friend-request/cancel/(?P<id>[\w-]+)/$', views.cancel_friend_request),
#     url(r'^friend-request/accept/(?P<id>[\w-]+)/$', views.accept_friend_request),
#     url(r'^friend-request/delete/(?P<id>[\w-]+)/$', views.delete_friend_request),
# ]

urlpatterns = [
    path('', views.users_list, name='list'),
    path('<slug>/', views.profile_view),
    path('friend-request/send/<id>/', views.send_friend_request),
    path('friend-request/cancel/<id>/', views.cancel_friend_request),
    path('friend-request/accept/<id>/', views.accept_friend_request),
    path('friend-request/delete/<id>/', views.delete_friend_request),
]
