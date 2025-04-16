from api.serializers import BlogPostSerializer
from api.models import BlogPost
from rest_framework import generics

class BlogPostListAPIView(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer