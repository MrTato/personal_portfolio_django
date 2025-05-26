from rest_framework import serializers
from .models import BlogPost
from .models import Contact


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


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message', 'created_at']
        read_only_fields = ['created_at']
