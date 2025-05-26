from django.db import models
from markdownx.models import MarkdownxField
import os
from uuid import uuid4


def blog_cover_image_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"cover_{instance.slug}_{uuid4().hex[:8]}.{ext}"
    return os.path.join('blog_images', filename)


def blog_preview_image_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"preview_{instance.slug}_{uuid4().hex[:8]}.{ext}"
    return os.path.join('blog_images', filename)


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    content = MarkdownxField(blank=True)
    description = models.TextField(max_length=300)
    cover_image = models.ImageField(
        upload_to=blog_cover_image_upload_path,
        null=True,
        blank=True,
        help_text="1200x500 image recommended"
    )
    preview_image = models.ImageField(
        upload_to=blog_preview_image_upload_path,
        null=True,
        blank=True,
        help_text="150x150 image recommended"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, editable=False)
    published = models.BooleanField(default=False)
    spotlight = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False)

    def __str__(self):
        return f"{self.name} ({self.email})"
