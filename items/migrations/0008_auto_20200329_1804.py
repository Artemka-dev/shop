# Generated by Django 2.2.11 on 2020-03-29 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0007_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.IntegerField(blank=True, db_index=True, verbose_name='Категория товара'),
        ),
    ]