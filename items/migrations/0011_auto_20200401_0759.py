# Generated by Django 2.2.11 on 2020-04-01 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0010_auto_20200330_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(db_index=True, verbose_name='Цена товара'),
        ),
    ]
