# Generated by Django 3.2.6 on 2021-12-27 18:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('Phone', models.CharField(max_length=10, unique=True)),
                ('First_Name', models.CharField(max_length=50)),
                ('Last_Name', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Phone', models.CharField(max_length=10)),
                ('otp', models.CharField(blank=True, max_length=6, null=True)),
                ('date', models.FloatField(default=1640631380.0559726)),
                ('First_Name', models.CharField(max_length=50)),
                ('Last_Name', models.CharField(max_length=50)),
                ('is_validate', models.BooleanField(blank=True, default=False, null=True)),
                ('video', models.CharField(blank=True, max_length=500, null=True)),
                ('is_video_validated', models.BooleanField(default=False)),
                ('bio', models.TextField(blank=True, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='images.png', null=True, upload_to='Profile_pics')),
                ('is_private', models.BooleanField(default=True)),
                ('request_receive', models.ManyToManyField(related_name='request_receive', to=settings.AUTH_USER_MODEL)),
                ('request_sent', models.ManyToManyField(related_name='request_sent', to=settings.AUTH_USER_MODEL)),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
