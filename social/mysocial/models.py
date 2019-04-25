from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation

class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='likes',
                             on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

class Post(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True, width_field="width_field", height_field="height_field")
    height_field=models.IntegerField(default=330)
    width_field = models.IntegerField(default=330)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    likes = GenericRelation(Like)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.likes

    def __repr__(self):
        return self.likes

    @property
    def total_likes(self):
        return self.likes.count()