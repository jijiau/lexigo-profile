# Generated by Django 5.1.3 on 2024-11-14 02:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_profile_profile_image_profile_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_picture',
        ),
    ]
