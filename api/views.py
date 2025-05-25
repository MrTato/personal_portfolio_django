from api.serializers import BlogPostSerializer
from api.serializers import ContactSerializer
from api.models import BlogPost
from api.models import Contact
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny


class BlogPostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogPost.objects.filter(published=True).order_by('-created_at')
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'


class ContactViewSet(mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]
