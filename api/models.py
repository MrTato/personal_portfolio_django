from django.db import models
from django.utils import timezone

# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, editable=False)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
