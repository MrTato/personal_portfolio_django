from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from api.models import BlogPost

# Register your models here.
class BlogPostAdmin(MarkdownxModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    class Media:
        css = {
            'all': ('css/admin_custom.css',)
        }

admin.site.register(BlogPost, BlogPostAdmin)