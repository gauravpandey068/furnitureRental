# Generated by Django 4.0 on 2022-01-09 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_rent_product_rent_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='rental_day',
            field=models.IntegerField(default=0),
        ),
    ]
