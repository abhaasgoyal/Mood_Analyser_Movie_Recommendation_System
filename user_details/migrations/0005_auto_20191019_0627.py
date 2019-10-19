# Generated by Django 2.2.6 on 2019-10-19 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_details', '0004_users_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='sex',
            field=models.CharField(choices=[('m', 'Male'), ('f', 'Female')], default='m', max_length=1),
        ),
    ]
