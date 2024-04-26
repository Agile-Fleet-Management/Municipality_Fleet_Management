# Generated by Django 4.2.6 on 2024-04-26 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Vehicles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maintenance',
            name='vehicle_id',
        ),
        migrations.AddField(
            model_name='maintenance',
            name='vehicle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Vehicles.vehicle'),
        ),
    ]
