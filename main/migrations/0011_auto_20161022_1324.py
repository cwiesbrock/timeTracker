# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-22 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20161022_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='begin',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='end',
            field=models.DateTimeField(blank=True, default=None),
        ),
    ]
