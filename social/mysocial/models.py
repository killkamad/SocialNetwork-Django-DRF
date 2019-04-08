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


# class Friend(models.Model):
#     users=models.ManyToManyField(User)
#     current_user=models.ForeignKey(User, related_name='owner', null=True, on_delete=models.CASCADE)
#
#     @classmethod
#     def make_friend(cls, current_user, new_friend):
#         friend, created = cls.objects.get_or_create(
#             current_user=current_user
#         )
#         friend.users.add(current_user, new_friend)
#
#     @classmethod
#     def lose_friend(cls, current_user, new_friend):
#         friend, created = cls.objects.get_or_create(
#             current_user=current_user
#         )
#         friend.users.remove(current_user, new_friend)
