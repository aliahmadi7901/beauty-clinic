from django.db import models


class Services(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان سرویس')
    short_description = models.CharField(max_length=400, verbose_name='توضیحات کوتاه')
    description = models.TextField(verbose_name='توضیحات کامل')
    image = models.ImageField(upload_to='services', verbose_name='تصویر سرویس')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'سرویس'
        verbose_name_plural = 'سرویس ها'
