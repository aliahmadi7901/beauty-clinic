from django.urls import path

from user_panel import views

urlpatterns = [
    path('', views.user_panel, name='user_panel'),
    path('edit-profile/', views.EditProfileView.as_view(), name='edit_profile'),
    path('change-password/', views.ChangePasswordView.as_view(), name='change_password'),
]
