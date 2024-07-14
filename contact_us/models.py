from django.db import models


class ContactUs(models.Model):
    address = models.CharField(max_length=300, verbose_name='آدرس')
    phone_1 = models.IntegerField(verbose_name='تلفن 1')
    phone_2 = models.IntegerField(verbose_name='تلفن 2(اختیاری)', blank=True, null=True)
    email_1 = models.EmailField(verbose_name='ایمیل 1')
    email_2 = models.EmailField(verbose_name='ایمیل 2(اختیاری)', blank=True, null=True)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'تماس با ما'


class ContactForm(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام')
    phone = models.IntegerField(verbose_name='شماره تماس')
    message = models.TextField(verbose_name='متن پیام')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'فرم تماس با ما'
        verbose_name_plural = 'فرم های تماس با ما'
