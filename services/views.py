from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from services.models import Services


class ServicesListView(ListView):
    model = Services
    context_object_name = 'services'
    template_name = 'services/services.html'
    paginate_by = 6

    def get_queryset(self):
        queryset = super(ServicesListView, self).get_queryset()
        title = self.request.GET.get('search', None)
        if title is not None:
            queryset = queryset.filter(title__icontains=title)

        return queryset


class ServicesDetailView(DetailView):
    model = Services
    context_object_name = 'service'
    template_name = 'services/service_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['services'] = Services.objects.order_by('-id')[:6]
        return context
