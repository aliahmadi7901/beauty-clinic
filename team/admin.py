from django.contrib import admin

from team.models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'skill', 'email', 'history')
    search_fields = ('name', 'skill', 'email')
    list_filter = ('skill',)
