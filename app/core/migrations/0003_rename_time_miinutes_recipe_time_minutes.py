# Generated by Django 3.2.25 on 2025-06-08 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_recipe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='time_miinutes',
            new_name='time_minutes',
        ),
    ]
