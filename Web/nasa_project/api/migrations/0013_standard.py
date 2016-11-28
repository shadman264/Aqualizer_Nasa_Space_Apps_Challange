# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 23:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20160420_2223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Standard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('from_ph', models.FloatField(blank=True, null=True)),
                ('to_ph', models.FloatField(blank=True, null=True)),
                ('from_temperature', models.FloatField(blank=True, null=True)),
                ('to_temperature', models.FloatField(blank=True, null=True)),
                ('from_orp', models.FloatField(blank=True, null=True)),
                ('to_orp', models.FloatField(blank=True, null=True)),
                ('from_salinity', models.FloatField(blank=True, null=True)),
                ('to_salinity', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]