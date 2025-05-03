from api.serializers import BlogPostSerializer
from api.models import BlogPost
from rest_framework import viewsets


class BlogPostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogPost.objects.filter(published=True).order_by('-created_at')
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
