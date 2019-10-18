# Generated by Django 2.2.6 on 2019-10-18 22:17

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('filmstars', '__first__'),
        ('movie_details', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='latest_news',
            fields=[
                ('news_id', models.IntegerField(default='', primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(0)])),
                ('news_message', models.TextField(max_length=255)),
                ('title', models.TextField(max_length=30)),
                ('images', models.TextField(max_length=255)),
                ('news_dt', models.DateTimeField()),
                ('actor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filmstars.filmstars')),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_details.movie_details')),
            ],
        ),
    ]
