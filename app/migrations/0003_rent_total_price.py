# Generated by Django 4.0 on 2022-01-08 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rent'),
    ]

    operations = [
        migrations.AddField(
            model_name='rent',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
