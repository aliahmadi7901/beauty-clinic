from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام پزشک')
    skill = models.CharField(max_length=100, verbose_name='مهارت و تخصص')
    image = models.ImageField(upload_to='doctors', verbose_name='تصویر پزشک')
    description = models.TextField(verbose_name='توضیخات در مورد پزشک')
    email = models.EmailField(verbose_name='ایمیل پزشک')
    office_phone = models.CharField(max_length=11, verbose_name='شماره مطب پزشک')
    history = models.IntegerField(verbose_name='سابقه پزشک /چند سال')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'پزشک'
        verbose_name_plural = 'پزشکان'
