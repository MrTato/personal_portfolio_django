from api.serializers import BlogPostSerializer
from api.serializers import ContactSerializer
from api.models import BlogPost
from api.models import Contact
from rest_framework import status, mixins, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.conf import settings
import requests
from django.core.mail import send_mail


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

        if not settings.DEBUG:
            contact = serializer.instance
            subject = f"📬 New Contact from {contact.name}"
            message = (
                f"Name: {contact.name}\n"
                f"Email: {contact.email}\n"
                f"Phone: {contact.phone or 'N/A'}\n\n"
                f"Message:\n{contact.message}"
            )

            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_RECIPIENT_EMAIL],
                fail_silently=False,
            )

            subject = f"📬 Submission confirmation"
            message = f'''
Hi {contact.name},

Thank you for getting in touch! I’ve received your message and will get back to you as soon as possible. If your inquiry is urgent, feel free to reply to this email directly.

Here’s a copy of what you submitted:

------------------------------------------------------------
📧 Email: {contact.email}
{f"📞 Phone: {contact.phone}" if contact.phone else ""}

📝 Message:
{contact.message}
------------------------------------------------------------

In the meantime, feel free to explore more of my work at https://bayardolopez.com

Warm regards,  
Bayardo López  
            '''

            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [contact.email],
                fail_silently=False,
            )

        return Response(serializer.data, status=status.HTTP_201_CREATED)
