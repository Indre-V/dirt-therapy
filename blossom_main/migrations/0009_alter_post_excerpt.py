# Generated by Django 4.2.13 on 2024-06-09 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blossom_main', '0008_post_comment_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
