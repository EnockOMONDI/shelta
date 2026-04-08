from django.contrib import admin
from .models import BlogPost, Project, Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'featured', 'sort_order')
    list_filter = ('featured',)
    search_fields = ('title', 'short_description')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'sector', 'slug', 'featured', 'sort_order')
    list_filter = ('featured', 'sector')
    search_fields = ('title', 'sector', 'summary')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'published_label', 'featured', 'sort_order')
    list_filter = ('featured',)
    search_fields = ('title', 'excerpt', 'intro', 'body')
    prepopulated_fields = {'slug': ('title',)}
