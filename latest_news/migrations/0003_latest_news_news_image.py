# Generated by Django 2.2.6 on 2019-10-29 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('latest_news', '0002_remove_latest_news_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='latest_news',
            name='news_image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
