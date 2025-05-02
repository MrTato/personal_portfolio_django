from api.serializers import BlogPostSerializer
from api.models import BlogPost
from rest_framework import viewsets
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly
)

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'
