import random

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
from django.views.generic import View

from account.forms import RegistrationForm, ConfirmationForm, LoginForm, ForgotForm, ResetPasswordForm
from account.models import User
from utils.send_email import send_email


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
                    register_form.add_error(
                        'email',
                        'حساب کاربری از قبل موجود است.اگر موفق به فعال سازی '
                        'حساب نشده اید از بخش فراموشی رمز عبور استفاده کنید.'
                    )
                else:
                    new_user = User(
                        email=email, email_active_code=random.randint(100000, 1000000),
                        username=email, is_active=False
                    )
                    new_user.set_password(password)
                    new_user.save()
                    send_email(
                        'کد فعال سازی حساب', new_user.email,
                        {'user': new_user}, 'email/email_active.html'
                    )
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


class ForgotView(View):
    def get(self, request, *args, **kwargs):
        forgot_form = ForgotForm()
        context = {'forgot_form': forgot_form}
        return render(request, 'account/forgot.html', context)

    def post(self, request, *args, **kwargs):
        forgot_form = ForgotForm(request.POST)
        if forgot_form.is_valid():
            email = forgot_form.cleaned_data.get('email', None)
            if email is None:
                forgot_form.add_error('email', 'ایمیل را وارد کنید!')
            else:
                current_user = User.objects.filter(email__iexact=email).first()
                if not current_user:
                    forgot_form.add_error(
                        'email', 'کاربری با ایمیل وارد شده یافت نشد یا کاربر غیر فعال می باشد!'
                    )
                else:
                    send_email(
                        'کد فراموشی رمز عبور', current_user.email,
                        {'user': current_user}, 'email/email_forget.html'
                    )
                    reset_form = ResetPasswordForm(initial={'email': current_user.email})
                    context = {'reset_form': reset_form}
                    return render(request, 'account/reset_password.html', context)

        context = {'forgot_form': forgot_form}
        return render(request, 'account/forgot.html', context)


class ResetPasswordView(View):
    def get(self, request, *args, **kwargs):
        reset_form = ResetPasswordForm()
        context = {'reset_form': reset_form}
        return render(request, 'account/reset_password.html', context)

    def post(self, request, *args, **kwargs):
        reset_form = ResetPasswordForm(request.POST)
        if reset_form.is_valid():
            email = reset_form.cleaned_data.get('email', None)
            code = reset_form.cleaned_data.get('code', None)
            password = reset_form.cleaned_data.get('password', None)
            if email and code and password is None:
                reset_form.add_error('code', 'اطلاعات وارد شده کافی نمی باشد!')
            else:
                current_user = User.objects.filter(email__iexact=email).first()
                if not current_user:
                    reset_form.add_error('code', 'کاربری یافت نشد!')
                else:
                    if current_user.email_active_code != code:
                        reset_form.add_error('code', 'کد وارد شده صحیح نیست!')
                    else:
                        current_user.set_password(password)
                        current_user.is_active = True
                        current_user.email_active_code = random.randint(100000, 1000000)
                        current_user.save()
                        login_form = LoginForm()
                        context = {'login_form': login_form}
                        return render(request, 'account/login.html', context)

        context = {'reset_form': reset_form}
        return render(request, 'account/reset_password.html', context)


class ResentCodePasswordView(View):
    def get(self, request, email, *args, **kwargs):
        user = User.objects.filter(email__iexact=email).first()
        if user is None:
            Http404('کاربری با این ایمیل یافت نشد!')
        else:
            user.email_active_code = random.randint(100000, 1000000)
            user.save()
            send_email(
                'کد فراموشی رمز عبور', user.email,
                {'user': user}, 'email/email_forget.html'
            )
            reset_form = ResetPasswordForm(initial={'email': user.email})
            context = {'reset_form': reset_form}
            return render(request, 'account/reset_password.html', context)


class ResentCodeRegisterView(View):
    def get(self, request, email, *args, **kwargs):
        user = User.objects.filter(email__iexact=email).first()
        if user is None:
            Http404('کاربری با این ایمیل یافت نشد!')
        else:
            user.email_active_code = random.randint(100000, 1000000)
            user.save()
            send_email(
                'کد فعال سازی حساب', user.email,
                {'user': user}, 'email/email_active.html'
            )
            confirm_form = ConfirmationForm(initial={'email': user.email})
            context = {'confirm_form': confirm_form}
            return render(request, 'account/confirm.html', context)


@method_decorator(login_required, name='dispatch')
class LogOut(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login_page')
