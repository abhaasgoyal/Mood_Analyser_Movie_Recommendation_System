# Generated by Django 2.2.6 on 2019-10-19 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_details', '0005_auto_20191019_0627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='profile_picture',
            field=models.CharField(default='blank.png', max_length=30),
        ),
    ]
