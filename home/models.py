from django.db import models


class Home(models.Model):
    image_home = models.ImageField(upload_to='home', verbose_name='تصویر صفحه اصلی')
    video_url = models.URLField(max_length=500, verbose_name='url فیلم تبلیغاتی')
    image_before_after = models.ImageField(upload_to='before_after', verbose_name='عکس قبل و بعد عمل')
    logo = models.ImageField(upload_to='logo', verbose_name='لوگوی سایت')
    footer_text = models.TextField(verbose_name='متن انتهای صفحات')
    copy_right_text = models.CharField(max_length=300, verbose_name='متن کپی رایت')

    def __str__(self):
        str(self.image_home)

    class Meta:
        verbose_name = 'صفحه اصلی'
        verbose_name_plural = 'صفحه اصلی'

