# Generated by Django 4.2.6 on 2024-05-06 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Vehicles', '0005_alter_vehicle_tool'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle',
            old_name='tool',
            new_name='transport',
        ),
    ]