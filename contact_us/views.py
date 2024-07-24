from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView

from contact_us.forms import ContactUsForm
from contact_us.models import ContactUs


class ContactUsView(View):
    def get(self, request, *args, **kwargs):
        contact_us = ContactUs.objects.last()
        contact_us_form = ContactUsForm()
        return render(
            request, 'contact_us/contact_us.html',
            {'contact_us': contact_us, 'contact_us_form': contact_us_form}
        )

    def post(self, request, *args, **kwargs):
        contact_us_form = ContactUsForm(request.POST)
        if contact_us_form.is_valid():
            contact_us_form.save()

        contact_us = ContactUs.objects.last()
        return render(
            request, 'contact_us/contact_us.html',
            {'contact_us': contact_us, 'contact_us_form': contact_us_form}
        )

