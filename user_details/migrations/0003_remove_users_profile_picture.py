# Generated by Django 2.2.6 on 2019-10-19 00:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_details', '0002_remove_users_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='profile_picture',
        ),
    ]
