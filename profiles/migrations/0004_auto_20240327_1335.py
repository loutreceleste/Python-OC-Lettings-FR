# Generated by Django 3.0 on 2024-03-27 13:35

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0003_auto_20240326_1631'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewProfile',
            new_name='Profile',
        ),
    ]