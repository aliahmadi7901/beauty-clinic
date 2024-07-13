from django.shortcuts import render
from django.views.generic import View


class HeaderComponent(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'shared/header_component.html')


class FooterComponent(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'shared/footer_component.html')


class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home/home.html')
