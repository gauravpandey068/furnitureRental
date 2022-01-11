# Generated by Django 4.0 on 2022-01-09 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_rent_product_rent_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rent',
            name='product',
        ),
        migrations.AddField(
            model_name='rent',
            name='product',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app.product'),
            preserve_default=False,
        ),
    ]