from django.shortcuts import render
from django.views.generic import ListView, DetailView

from team.models import Doctor


class DoctorListView(ListView):
    model = Doctor
    context_object_name = 'doctors'
    template_name = 'team/team.html'
    paginate_by = 6


class DoctorDetailView(DetailView):
    model = Doctor
    context_object_name = 'doctor'
    template_name = 'team/team_detail.html'

