from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='ایمیل')
    password = models.CharField(max_length=50, verbose_name='رمز عبور')
    image = models.ImageField(upload_to='users', null=True, blank=True, verbose_name='تصویر کاربر')

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
