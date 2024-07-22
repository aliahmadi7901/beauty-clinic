from django.urls import path

from account import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register_page'),
    path('confirm/', views.ConfirmView.as_view(), name='confirm_page'),
    path('login/', views.LoginView.as_view(), name='login_page'),
    path('forgot/', views.ForgotView.as_view(), name='forgot_page'),
    path('reset-password/', views.ResetPasswordView.as_view(), name='reset_page'),
    path('resent-code-password/<str:email>/', views.ResentCodePasswordView.as_view(), name='resent_code_password'),
    path('resent-code-register/<str:email>/', views.ResentCodeRegisterView.as_view(), name='resent_code_register'),
    path('log-out/', views.LogOut.as_view(), name='logout_page'),
]
