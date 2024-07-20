from django import forms
from django.core.exceptions import ValidationError

from account.models import User


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'image']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'تصویر پروفایل'}),
        }
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'image': 'تصویر پروفایل',
        }


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبور فعلی'}),
        label='رمز عبور فعلی'
    )
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبور جدید'}),
        label='رمز عبور جدید'
    )
