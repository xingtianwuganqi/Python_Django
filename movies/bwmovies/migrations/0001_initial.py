# Generated by Django 2.2.6 on 2020-07-20 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dongzuopian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_type', models.CharField(max_length=30)),
                ('movie_name', models.CharField(max_length=100)),
                ('movie_star', models.IntegerField()),
                ('movie_actor', models.CharField(max_length=100)),
                ('movie_url', models.CharField(max_length=100)),
                ('movie_img', models.CharField(max_length=100)),
            ],
        ),
    ]