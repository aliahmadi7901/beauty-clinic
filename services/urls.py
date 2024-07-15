from django.urls import path

from services import views

urlpatterns = [
    path('', views.ServicesListView.as_view(), name='services_page'),
    path('<int:pk>/', views.ServicesDetailView.as_view(), name='service_detail'),
]
