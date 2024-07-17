from django.urls import path

from account import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register_page'),
    path('confirm/', views.ConfirmView.as_view(), name='confirm_page'),
    path('login/', views.LoginView.as_view(), name='login_page'),
]
