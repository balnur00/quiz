from rest_framework import serializers
from main.models import Post
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class PostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False)
    body = serializers.CharField(max_length=1000, required=True)
    like_count = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('__all__')


class LikeSerializer(serializers.ModelSerializer):
    like_count = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False)
    body = serializers.CharField(max_length=1000, required=False)

    class Meta:
        model = Post
        fields = ('__all__')
