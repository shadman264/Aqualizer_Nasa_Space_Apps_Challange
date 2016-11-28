# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-10 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20160410_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waterparticle',
            name='dateTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='waterparticle',
            name='deviceID',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='waterparticle',
            name='geoLocation',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='waterparticle',
            name='orp',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='waterparticle',
            name='ph',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='waterparticle',
            name='temperature',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='waterparticle',
            name='user',
            field=models.CharField(max_length=50, null=True),
        ),
    ]