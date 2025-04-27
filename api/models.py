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
