import random

from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic import View

from account.forms import RegistrationForm, ConfirmationForm, LoginForm
from account.models import User


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        register_form = RegistrationForm()
        context = {'register_form': register_form}
        return render(request, 'account/register.html', context)

    def post(self, request, *args, **kwargs):
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            email = register_form.cleaned_data.get('email', None)
            password = register_form.cleaned_data.get('password', None)
            if email and password is None:
                register_form.add_error('email', 'مقادیر لازم را پر کنید!')
            else:
                user = User.objects.filter(email__iexact=email).exists()
                if user:
                    register_form.add_error(email, 'حساب کاربری از قبل موجود است.')
                else:
                    new_user = User(
                        email=email, email_active_code=random.randint(100000, 1000000),
                        username=email, is_active=False
                    )
                    new_user.set_password(password)
                    new_user.save()
                    # send email
                    confirm_form = ConfirmationForm(initial={'email': new_user.email})
                    context = {'confirm_form': confirm_form}
                    return render(request, 'account/confirm.html', context)

        context = {'register_form': register_form}
        return render(request, 'account/register.html', context)


class ConfirmView(View):
    def get(self, request, *args, **kwargs):
        confirm_form = ConfirmationForm()
        context = {'confirm_form': confirm_form}
        return render(request, 'account/confirm.html', context)

    def post(self, request, *args, **kwargs):
        confirm_form = ConfirmationForm(request.POST)
        if confirm_form.is_valid():
            code = confirm_form.cleaned_data.get('code', None)
            email = confirm_form.cleaned_data.get('email', None)
            if code is None:
                confirm_form.add_error('code', 'کد را وارد کنید!')
            else:
                current_user = User.objects.filter(email=email).first()
                if current_user is None:
                    confirm_form.add_error('code', 'کاربری با مشخصات وارد شده یافت نشد!')
                else:
                    if current_user.email_active_code != code:
                        confirm_form.add_error('code', 'کد وارد شده صحیح نیست!')
                    else:
                        current_user.is_active = True
                        current_user.email_active_code = random.randint(100000, 1000000)
                        current_user.save()
                        login_form = LoginForm()
                        context = {'login_form': login_form}
                        return render(request, 'account/login.html', context)

        context = {'confirm_form': confirm_form}
        return render(request, 'account/confirm.html', context)


class LoginView(View):
    def get(self, request, *args, **kwargs):
        login_form = LoginForm()
        context = {'login_form': login_form}
        return render(request, 'account/login.html', context)

    def post(self, request, *args, **kwargs):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data.get('email', None)
            password = login_form.cleaned_data.get('password', None)
            if email and password is None:
                login_form.add_error('email', 'مقادیر لازم را پر کنید!')
            else:
                current_user = User.objects.filter(email__iexact=email, is_active=True).first()
                if current_user is None:
                    login_form.add_error('email', 'حساب کاربری با این ایمیل یافت نشد یا حساب غیر فعال است!')
                else:
                    check_password = current_user.check_password(password)
                    if not check_password:
                        login_form.add_error('password', 'رمز عبور اشتباه است!')
                    else:
                        login(request, current_user)
                        return redirect('home_page')

        context = {'login_form': login_form}
        return render(request, 'account/login.html', context)
