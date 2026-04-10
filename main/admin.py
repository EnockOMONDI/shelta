from django.contrib import admin
from django.http import HttpResponse
from unfold.admin import ModelAdmin

from .models import BlogPost, CompanyProfile, ProfileDownloadLead, Project, Service


def export_leads_as_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="profile-download-leads.csv"'
    response.write('email,source,ip_address,sent_at,created_at\n')
    for lead in queryset:
        response.write(
            f'"{lead.email}","{lead.source}","{lead.ip_address or ""}","{lead.sent_at or ""}","{lead.created_at}"\n'
        )
    return response


export_leads_as_csv.short_description = 'Export selected leads as CSV'


@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    list_display = ('title', 'slug', 'featured', 'sort_order')
    list_filter = ('featured',)
    search_fields = ('title', 'short_description')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    list_display = ('title', 'sector', 'slug', 'featured', 'sort_order')
    list_filter = ('featured', 'sector')
    search_fields = ('title', 'sector', 'summary')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(BlogPost)
class BlogPostAdmin(ModelAdmin):
    list_display = ('title', 'slug', 'author', 'published_label', 'featured', 'sort_order')
    list_filter = ('featured',)
    search_fields = ('title', 'excerpt', 'intro', 'body')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(CompanyProfile)
class CompanyProfileAdmin(ModelAdmin):
    list_display = ('title', 'is_active', 'download_url', 'uploadcare_file_id', 'updated_at')
    list_filter = ('is_active',)
    search_fields = ('title', 'download_url', 'uploadcare_file_id')


@admin.register(ProfileDownloadLead)
class ProfileDownloadLeadAdmin(ModelAdmin):
    list_display = ('email', 'source', 'ip_address', 'sent_at', 'created_at')
    list_filter = ('source', 'sent_at', 'created_at')
    search_fields = ('email', 'user_agent', 'source')
    readonly_fields = ('email', 'source', 'ip_address', 'user_agent', 'sent_at', 'created_at')
    actions = [export_leads_as_csv]
