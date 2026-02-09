from django.contrib import admin
from .models import HairStyle, Comment, SiteAnalytics

# Branding for the Admin Dashboard
admin.site.site_header = "The Queens Touch Royal Dashboard"
admin.site.site_title = "The Queens Touch Admin"
admin.site.index_title = "Welcome to the Royal Management Suite"

@admin.register(HairStyle)
class HairStyleAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created_at')
    search_fields = ('title',)
    list_filter = ('created_at',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # Displays the reviewer name and date in the list view
    list_display = ('name', 'created_at', 'message_excerpt')
    list_filter = ('created_at',)
    search_fields = ('name', 'message')

    # A genius trick to show just a preview of the message in the list
    def message_excerpt(self, obj):
        return obj.message[:50] + "..." if len(obj.message) > 50 else obj.message
    message_excerpt.short_description = "Message Preview"

@admin.register(SiteAnalytics)
class SiteAnalyticsAdmin(admin.ModelAdmin):
    list_display = ('total_visits', 'whatsapp_clicks', 'review_submissions')
    
    # Prevents creating more than one analytics row or deleting the data
    def has_add_permission(self, request):
        return False if SiteAnalytics.objects.exists() else True

    def has_delete_permission(self, request, obj=None):
        return False