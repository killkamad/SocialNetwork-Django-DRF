from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True, width_field="width_field", height_field="height_field")
    height_field=models.IntegerField(default=330)
    width_field = models.IntegerField(default=330)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     description = models.CharField(max_length=100, default='')
#     city = models.CharField(max_length=100, default='')
#     website = models.URLField(default='')
#     phone = models.IntegerField(default=0)
#     image = models.ImageField(upload_to='profile_image', blank=True)
#
#     def get_connections(self):
#         connections = Connection.objects.filter(creator=self.user)
#         return connections
#
#     def get_followers(self):
#         followers = Connection.objects.filter(following=self.user)
#         return followers

# class Friend(models.Model):
#     users = models.ManyToManyField(UserProfile)
#     current_user=models.ForeignKey(UserProfile, related_name='owner', null=True, on_delete=models.CASCADE)
#
#     @classmethod
#     def make_friend(cls, current_user, new_friend):
#         friend, created = cls.objects.get_or_create(
#             current_user=current_user
#         )
#         friend.users.add(new_friend)
#
#     @classmethod
#     def remove_friend(cls, current_user, new_friend):
#         friend, created = cls.objects.get_or_create(
#             current_user=current_user
#         )
#         friend.users.remove(new_friend)
#
#     def __str__(self):
#         return str(self.current_user)

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save


# class Profile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     slug = models.SlugField()
#     friends = models.ManyToManyField("Profile", blank=True)
#
#     def __str__(self):
#         return str(self.user.username)
#
#     def get_absolute_url(self):
#     	return "/users/{}".format(self.slug)
#
#
# def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
#     if created:
#         try:
#             Profile.objects.create(user=instance)
#         except:
#             pass
#
# post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)
#
#
# class FriendRequest(models.Model):
# 	to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='to_user', on_delete=models.CASCADE)
# 	from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='from_user',  on_delete=models.CASCADE)
# 	timestamp = models.DateTimeField(auto_now_add=True) # set when created
#
# 	def __str__(self):
# 		return "From {}, to {}".format(self.from_user.username, self.to_user.username)