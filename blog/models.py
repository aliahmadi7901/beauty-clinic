from django.db import models
from django_jalali.db import models as jmodels

from account.models import User


class BlogCategory(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان دسته بندی')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی مقاله'
        verbose_name_plural = 'دسته بندی مقالات'


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان مقاله')
    image = models.ImageField(upload_to='blogs', verbose_name='تصویر مقاله')
    short_description = models.CharField(max_length=300, verbose_name='توضیحات کوتاه مقاله')
    description = models.TextField(verbose_name='توضیحات کامل مقاله')
    category = models.ForeignKey(
        BlogCategory, on_delete=models.CASCADE, related_name='blogs', verbose_name='دسته بندی مقاله'
    )
    active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')

    created_at = jmodels.jDateTimeField(auto_now_add=True, verbose_name='زمان ساخت')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'


class BlogComment(models.Model):
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name='blog_comments', verbose_name='مقاله'
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments', verbose_name='کاربر'
    )
    comment = models.TextField(verbose_name='نظر')
    created_at = jmodels.jDateTimeField(auto_now_add=True, verbose_name='زمان ساخت')

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = 'نظر مقاله'
        verbose_name_plural = 'نظرات مقاله'
