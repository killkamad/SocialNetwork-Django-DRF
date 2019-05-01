from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.users_list, name='list'),
    path('<slug>/', views.profile_view),
    path('friend-request/send/<id>/', views.send_friend_request),
    path('friend-request/cancel/<id>/', views.cancel_friend_request),
    path('friend-request/accept/<id>/', views.accept_friend_request),
    path('friend-request/delete/<id>/', views.delete_friend_request),
]
