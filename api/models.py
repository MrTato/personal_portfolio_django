from django.db import models
from markdownx.models import MarkdownxField

# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    content = MarkdownxField(blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, editable=False)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class BlogPostImage(models.Model):
    blog_post = models.ForeignKey(
        'BlogPost', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_images/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.caption or self.image.name
