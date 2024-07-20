from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View

from account.models import User
from user_panel.forms import EditProfileForm, ChangePasswordForm


@login_required
def user_panel(request):
    return render(request, 'user_panel/user_panel.html')


@login_required
def user_panel_menu(request):
    return render(request, 'user_panel/user_panel_menu.html')


@method_decorator(login_required, name='dispatch')
class EditProfileView(View):
    def get(self, request, *args, **kwargs):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_form = EditProfileForm(instance=current_user)
        return render(request, 'user_panel/edit_profile.html', {
            'current_user': current_user, 'edit_form': edit_form
        })

    def post(self, request, *args, **kwargs):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_form = EditProfileForm(request.POST, request.FILES, instance=current_user)
        if edit_form.is_valid():
            edit_form.save(commit=True)

        return render(request, 'user_panel/edit_profile.html', {
            'current_user': current_user, 'edit_form': edit_form
        })


@method_decorator(login_required, name='dispatch')
class ChangePasswordView(View):
    def get(self, request, *args, **kwargs):
        change_password_form = ChangePasswordForm()
        context = {'change_password_form': change_password_form}
        return render(request, 'user_panel/change_password.html', context=context)

    def post(self, request, *args, **kwargs):
        current_user: User = User.objects.filter(id=request.user.id).first()
        if current_user is None:
            return HttpResponse('کاربری با مشخصات وارد شده یافت نشد!')

        change_password_form = ChangePasswordForm(request.POST)
        if change_password_form.is_valid():
            current_password = change_password_form.cleaned_data.get('current_password')
            if current_user.check_password(current_password):
                current_user.set_password(change_password_form.cleaned_data.get('new_password'))
                current_user.save()
                logout(self.request)
                return redirect(reverse('login_page'))
            else:
                change_password_form.add_error('current_password', 'رمز عبور وارد شده نامعتبر است!')

        context = {'change_password_form': change_password_form}
        return render(request, 'user_panel/change_password.html', context=context)
