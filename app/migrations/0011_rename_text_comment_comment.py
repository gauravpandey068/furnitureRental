# Generated by Django 4.0 on 2022-01-12 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='text',
            new_name='comment',
        ),
    ]
