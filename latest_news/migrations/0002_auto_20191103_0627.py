# Generated by Django 2.2.6 on 2019-11-03 06:27

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('latest_news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='latest_news',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='latest_news',
            name='news_dt',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 3, 6, 27, 7, 383987, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='latest_news',
            name='news_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='latest_news',
            name='news_message',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='latest_news',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]