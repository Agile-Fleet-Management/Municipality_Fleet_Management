# Generated by Django 5.0.4 on 2024-04-23 15:51

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Vehicles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='asmae', max_length=20)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('status', models.CharField(choices=[(1, 'On Going'), (2, 'Arrived'), (3, 'OverDue'), (4, 'Pending'), (5, 'Approved'), (6, 'Rejected')], default=4)),
                ('expected_arrival', models.DateTimeField(max_length=20)),
                ('request_time', models.DateTimeField(default=datetime.datetime.now)),
                ('description', models.CharField(max_length=500)),
                ('requester_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vehicle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vehicles.vehicle')),
                ('mission_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='missions.mission')),
            ],
            options={
                'unique_together': {('mission_id', 'vehicle_id')},
            },
        ),
        migrations.CreateModel(
            name='MissionParticipant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mission_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='missions.mission')),
                ('participant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('mission_id', 'participant_id')},
            },
        ),
    ]
