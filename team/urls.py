from django.urls import path

from team import views

urlpatterns = [
    path('', views.DoctorListView.as_view(), name='team_page'),
    path('<int:pk>/', views.DoctorDetailView.as_view(), name='doctor_page'),
]
