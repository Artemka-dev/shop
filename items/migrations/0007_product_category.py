# Generated by Django 2.2.11 on 2020-03-29 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0006_auto_20200329_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.TextField(blank=True, db_index=True, verbose_name='Категория товара'),
        ),
    ]
