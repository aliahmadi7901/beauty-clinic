from django.contrib import admin

from home.models import SiteSettings, Home


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('image_home', 'video_url', 'image_before_after')


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('copy_right_text', 'text_footer')
