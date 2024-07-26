from django.shortcuts import render
from django.views.generic import View

from blog.models import Blog
from contact_us.models import ContactUs
from home.models import SiteSettings, Home
from services.models import Services
from team.models import Doctor


class HeaderComponent(View):
    def get(self, request, *args, **kwargs):
        site_setting = SiteSettings.objects.last()
        contact_us = ContactUs.objects.last()
        return render(
            request, 'shared/header_component.html',
            {'site_setting': site_setting, 'contact_us': contact_us}
        )


class FooterComponent(View):
    def get(self, request, *args, **kwargs):
        site_setting = SiteSettings.objects.last()
        services = Services.objects.all()
        return render(
            request, 'shared/footer_component.html',
            {'site_setting': site_setting, 'services': services}
        )


class HomeView(View):
    def get(self, request, *args, **kwargs):
        services = Services.objects.order_by('?')[:4]
        home = Home.objects.last()
        doctors = Doctor.objects.order_by("?")[:3]
        contact_us = ContactUs.objects.last()
        current_blogs = Blog.objects.order_by('-id')[:3]
        return render(
            request, 'home/home.html',
            {'services': services, 'home': home, 'doctors': doctors,
             'contact_us': contact_us, 'current_blogs': current_blogs}
        )
