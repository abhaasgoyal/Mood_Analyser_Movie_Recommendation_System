# Generated by Django 2.2.6 on 2019-10-29 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_details', '0015_auto_20191030_0451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile_info',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='user_images/'),
        ),
    ]