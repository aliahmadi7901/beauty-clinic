# Generated by Django 5.0.7 on 2024-07-22 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogcomment_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcomment',
            name='answer',
        ),
    ]
