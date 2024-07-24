from django.db import models


class AboutUs(models.Model):
    title_about_us = models.CharField(max_length=300, verbose_name='عنوان صفحه درباره ما')
    text_about_us = models.TextField(verbose_name='متن صفحه درباره ما')
    image_about_us = models.ImageField(upload_to='about_us', verbose_name='تصویر صفجه درباره ما')

    def __str__(self):
        return self.title_about_us

    class Meta:
        verbose_name = 'درباره ما'
        verbose_name_plural = 'درباره ما'


class GrowthHistory(models.Model):
    year = models.IntegerField(verbose_name='سال وقوع اتفاق')
    title = models.CharField(max_length=200, verbose_name='عنوان اتفاق')
    text = models.TextField(verbose_name='متن اتفاق')
    image = models.ImageField(upload_to='history', verbose_name='تصویر اتفاق')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تاریخچه رشد'
        verbose_name_plural = 'تاریخچه های رشد'


class Advantages(models.Model):
    text = models.TextField(verbose_name='متن مزایای کلینیک')
    image_1 = models.ImageField(upload_to='about_us', verbose_name='تصویر اول')
    image_2 = models.ImageField(upload_to='about_us', verbose_name='تصویر دوم')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'مزیت'
        verbose_name_plural = 'مزایا'



class Questions(models.Model):
    question = models.TextField(verbose_name='سوال متدوال')
    answer = models.TextField(verbose_name='پاسخ سوال متدوال')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'سوال متداول'
        verbose_name_plural = 'سوالات متداول'
