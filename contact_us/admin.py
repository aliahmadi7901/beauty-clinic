from django.contrib import admin

from contact_us.models import ContactUs, ContactForm


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone_1', 'phone_2', 'email_1', 'email_2')


@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'message', 'is_read')
    list_filter = ('is_read', )
    search_fields = ('name', 'phone')
    list_editable = ('is_read', )
