# Generated by Django 2.2.6 on 2019-10-29 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0003_remove_forum_posts_news_dt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum_posts',
            name='images',
            field=models.ImageField(upload_to=''),
        ),
    ]