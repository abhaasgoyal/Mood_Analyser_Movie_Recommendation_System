# Generated by Django 2.2.6 on 2019-10-18 22:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_details', '0001_initial'),
        ('forums', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='replies',
            fields=[
                ('reply_id', models.IntegerField(default='', primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(0)])),
                ('reply_message', models.TextField(max_length=255)),
                ('reply_dt', models.DateTimeField(blank=True, null=True)),
                ('comment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forums.forum_posts')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_details.users')),
            ],
        ),
        migrations.CreateModel(
            name='comments',
            fields=[
                ('comment_id', models.IntegerField(default='', primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(0)])),
                ('comment_message', models.TextField(max_length=255)),
                ('comment_dt', models.DateTimeField(blank=True, null=True)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forums.forum_posts')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_details.users')),
            ],
        ),
    ]