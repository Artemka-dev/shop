# Generated by Django 2.2.11 on 2020-03-30 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0008_auto_20200329_1804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='product_to',
        ),
        migrations.AddField(
            model_name='basket',
            name='id_product',
            field=models.IntegerField(blank=True, db_index=True, null=True),
        ),
    ]
