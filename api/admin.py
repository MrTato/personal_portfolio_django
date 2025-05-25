from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from api.models import BlogPost, Contact


class BlogPostAdmin(MarkdownxModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

    class Media:
        css = {
            'all': ('css/admin_custom.css',)
        }


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    readonly_fields = ('name', 'email', 'phone', 'message', 'created_at')
    ordering = ('-created_at',)
    search_fields = ('name', 'email', 'message')

    def has_add_permission(self, request):
        return False


admin.site.register(BlogPost, BlogPostAdmin)
