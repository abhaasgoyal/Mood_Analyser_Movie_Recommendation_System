# Generated by Django 2.2.6 on 2019-11-03 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmstars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmstars',
            name='died',
            field=models.DateField(blank=True, max_length=8, null=True),
        ),
    ]
