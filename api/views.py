from api.serializers import BlogPostSerializer
from api.serializers import ContactSerializer
from api.models import BlogPost
from api.models import Contact
from rest_framework import status, mixins, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.conf import settings
import requests


class BlogPostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogPost.objects.filter(published=True).order_by('-created_at')
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'


class ContactViewSet(mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        if not settings.DEBUG:
            token = request.data.get('recaptchaToken')

            if token:
                secret = settings.RECAPTCHA_SECRET_KEY
                response = requests.post(
                    'https://www.google.com/recaptcha/api/siteverify',
                    data={'secret': secret, 'response': token}
                )
                result = response.json()

                if not result.get('success') or result.get('score', 0) < 0.5:
                    return Response({'detail': 'reCAPTCHA failed.'}, status=status.HTTP_403_FORBIDDEN)
            else:
                return Response({'detail': 'reCAPTCHA failed.'}, status=status.HTTP_403_FORBIDDEN)

        # continue normal creation
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
