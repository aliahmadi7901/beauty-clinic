from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام دکتر')
    skill = models.CharField(max_length=100, verbose_name='مهارت و تخصص')
    image = models.ImageField(upload_to='doctors', verbose_name='تصویر دکتر')
    description = models.TextField(verbose_name='توضیخات در مورد دکتر')
    email = models.EmailField(verbose_name='ایمیل دکتر')
    office_phone = models.IntegerField(verbose_name='شماره مطب دکتر')
    history = models.IntegerField(verbose_name='سابقه دکتر /چند سال')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'دکتر'
        verbose_name_plural = 'دکتر ها'
