# Generated by Django 4.2.13 on 2024-06-09 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blossom_main', '0007_alter_post_excerpt'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comment_count',
            field=models.IntegerField(default=0),
        ),
    ]
