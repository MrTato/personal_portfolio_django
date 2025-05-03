from api.serializers import BlogPostSerializer
from api.models import BlogPost
from rest_framework import viewsets

class BlogPostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
