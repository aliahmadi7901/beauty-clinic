from django.urls import path
from django.views.generic import TemplateView

from contact_us import views

urlpatterns = [
    path('', views.ContactUsView.as_view(), name='contact_us'),
]
