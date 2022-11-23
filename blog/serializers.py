from rest_framework import serializers
from .models import Post, Comment, PublishedManager

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = "__all__"


class CoomentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"


class PublishedManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = PublishedManager
        fields = "__all__"

