# Generated by Django 5.0.7 on 2024-07-25 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_site', models.ImageField(upload_to='logo', verbose_name='لوگوی سایت')),
                ('logo_footer', models.ImageField(upload_to='logo', verbose_name='لوگوی پایین صفحه')),
                ('text_footer', models.TextField(verbose_name='متن پایین صفحه')),
                ('copy_right_text', models.TextField(verbose_name='متن کپی رایت')),
            ],
            options={
                'verbose_name': 'تنظیم سایت',
                'verbose_name_plural': 'تنظیمات سایت',
            },
        ),
    ]
