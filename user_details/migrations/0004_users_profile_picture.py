# Generated by Django 2.2.6 on 2019-10-19 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_details', '0003_remove_users_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='profile_picture',
            field=models.CharField(default='', max_length=30),
        ),
    ]
