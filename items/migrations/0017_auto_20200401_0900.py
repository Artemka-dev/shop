# Generated by Django 2.2.11 on 2020-04-01 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0016_auto_20200401_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_public',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
