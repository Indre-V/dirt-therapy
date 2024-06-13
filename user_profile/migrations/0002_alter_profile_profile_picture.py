# Generated by Django 4.2.13 on 2024-06-13 21:19

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(default='images/placeholder_profile.jpg', max_length=255, verbose_name='image'),
        ),
    ]
