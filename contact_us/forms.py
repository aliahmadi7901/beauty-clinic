from django import forms

from contact_us.models import ContactForm


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['name', 'phone', 'message']
