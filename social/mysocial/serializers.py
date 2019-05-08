from rest_framework import serializers
from .models import Post

from . import views as likes_services
from django.contrib.auth import get_user_model

class PostSerializer(serializers.ModelSerializer):

    is_fan = serializers.SerializerMethodField()
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = (
            'author',
            'id',
            'title',
            'text',
            'created_date',
            'published_date',
            'total_likes',
            'is_fan',
			'image',
        )

    def get_is_fan(self, obj) -> bool:
        """Проверяет, лайкнул ли `request.user` твит (`obj`).
        """
        user = self.context.get('request').user
        return likes_services.is_fan(obj, user)

User = get_user_model()
class FanSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = (
            'username',
            'full_name',
        )
    def get_full_name(self, obj):
        return obj.get_full_name()