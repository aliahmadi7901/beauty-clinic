from django.contrib import admin

from blog.models import Blog, BlogCategory, BlogComment


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'active', 'category', 'created_at')
    list_filter = ('active', 'category')
    search_fields = ('title', 'short_description')
    list_editable = ('active',)


@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('blog', 'user', 'created_at', 'is_active')
    list_filter = ('blog',)
    search_fields = ('blog', 'user')
    list_editable = ('is_active',)
