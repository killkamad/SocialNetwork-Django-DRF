from django.contrib import admin
from .models import Post, Like
# from .models import Profile, FriendRequest
#
# admin.site.register(Profile)
# admin.site.register(FriendRequest)

admin.site.register(Post)
admin.site.register(Like)