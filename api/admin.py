from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from api.models import BlogPost

# Register your models here.
admin.site.register(BlogPost, MarkdownxModelAdmin)