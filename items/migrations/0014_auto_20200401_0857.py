# Generated by Django 2.2.11 on 2020-04-01 08:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0013_auto_20200401_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_public',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 1, 8, 57, 29, 94995, tzinfo=utc)),
        ),
    ]
