from django.db import models


class Home(models.Model):
    image_home = models.ImageField(upload_to='home', verbose_name='بنر صفحه اصلی')
    video_url = models.URLField(max_length=500, verbose_name='url فیلم تبلیغاتی')
    image_before_after = models.ImageField(upload_to='before_after', verbose_name='عکس قبل و بعد عمل')

    def __str__(self):
        return self.image_home.name

    class Meta:
        verbose_name = 'صفحه اصلی'
        verbose_name_plural = 'مدیریت صفحه اصلی'


class SiteSettings(models.Model):
    logo_site = models.ImageField(upload_to='logo', verbose_name='لوگوی سایت')
    logo_footer = models.ImageField(upload_to='logo', verbose_name='لوگوی پایین صفحه')
    text_footer = models.TextField(verbose_name='متن پایین صفحه')
    copy_right_text = models.TextField(verbose_name='متن کپی رایت')

    def __str__(self):
        return self.copy_right_text

    class Meta:
        verbose_name = 'تنظیم سایت'
        verbose_name_plural = 'تنظیمات سایت'

