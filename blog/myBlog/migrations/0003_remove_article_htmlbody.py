# Generated by Django 2.2.6 on 2020-07-17 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myBlog', '0002_auto_20200717_2203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='htmlbody',
        ),
    ]
