from django.shortcuts import render
from django.views.generic import ListView, DetailView

from services.models import Services


class ServicesListView(ListView):
    model = Services
    context_object_name = 'services'
    template_name = 'services/services.html'
    paginate_by = 6


class ServicesDetailView(DetailView):
    model = Services
    context_object_name = 'service'
    template_name = 'services/service_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['services'] = Services.objects.order_by('-id')[:6]
        return context
