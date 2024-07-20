from django import forms
from django.core import validators

from account.models import User


class RegistrationForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'ایمیل'}),
        validators=[validators.EmailValidator], label='ایمیل'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور'}),
        label='رمز عبور'
    )


class ConfirmationForm(forms.Form):
    code = forms.CharField(label='کد دریافتی از طریق ایمیل')
    email = forms.CharField(widget=forms.HiddenInput(), required=False)


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'ایمیل'}), validators=[validators.EmailValidator], label='ایمیل'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور'}),
        label='رمز عبور'
    )


class ForgotForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'ایمیل'}), validators=[validators.EmailValidator], label='ایمیل'
    )


class ResetPasswordForm(forms.Form):
    email = forms.CharField(widget=forms.HiddenInput(), required=False)
    code = forms.CharField(label='کد دریافتی از طریق ایمیل')
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور جدید'}),
        label='رمز عبور جدید'
    )
