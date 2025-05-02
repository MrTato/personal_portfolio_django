from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from api.models import BlogPost, BlogPostImage


class BlogPostImageInline(admin.TabularInline):
    model = BlogPostImage
    extra = 1


class BlogPostAdmin(MarkdownxModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    inlines = [BlogPostImageInline]

    class Media:
        css = {
            'all': ('css/admin_custom.css',)
        }


admin.site.register(BlogPost, BlogPostAdmin)
