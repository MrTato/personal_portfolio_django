from api.serializers import BlogPostSerializer
from api.models import BlogPost
from rest_framework import viewsets
from rest_framework.permissions import (
    AllowAny
)


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'
