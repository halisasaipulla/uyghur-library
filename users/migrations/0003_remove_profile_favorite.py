# Generated by Django 3.2.5 on 2021-08-16 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='favorite',
        ),
    ]