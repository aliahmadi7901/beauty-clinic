# Generated by Django 5.0.7 on 2024-07-26 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_sitesettings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='copy_right_text',
        ),
        migrations.RemoveField(
            model_name='home',
            name='footer_text',
        ),
        migrations.RemoveField(
            model_name='home',
            name='logo',
        ),
    ]
