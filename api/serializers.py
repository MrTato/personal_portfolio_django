from rest_framework import serializers
from .models import BlogPost, BlogPostImage


class BlogPostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPostImage
        fields = ['id', 'image', 'caption']


class BlogPostSerializer(serializers.ModelSerializer):
    images = BlogPostImageSerializer(many=True, read_only=True)

    class Meta:
        model = BlogPost
        fields = (
            'id',
            'title',
            'slug',
            'content',
            'created_at',
            'updated_at',
            'published',
            'images'
        )
