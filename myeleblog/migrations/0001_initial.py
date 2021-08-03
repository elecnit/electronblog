# Generated by Django 3.2.3 on 2021-08-03 10:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='images/profile/')),
                ('website_url', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('whatsapp_url', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('facebook_url', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('insta_url', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('twitter_url', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('header_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('body', models.TextField()),
                ('snippet', models.CharField(max_length=250)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
