from rest_framework import serializers
from .models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = (
            'title',
            'slug',
            'content',
            'description',
            'cover_image',
            'preview_image',
            'created_at',
            'updated_at',
            'spotlight',
        )
