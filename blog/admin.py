from django.contrib import admin
from blog.models import Tag, Post, Comment


admin.site.register(Tag)
admin.site.register(Comment)


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("slug", "published_at")


admin.site.register(Post, PostAdmin)