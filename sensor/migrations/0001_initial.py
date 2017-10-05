# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 13:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('device', '0003_auto_20171005_2120'),
        ('sensor_types', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SensorModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_id', models.CharField(max_length=17, unique=True)),
                ('pin', models.CharField(max_length=5)),
                ('devices', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.DeviceModel')),
                ('type', models.ForeignKey(db_column='type', on_delete=django.db.models.deletion.CASCADE, to='sensor_types.SensorTypeModel')),
            ],
            options={
                'db_table': 'sensors',
            },
        ),
    ]
