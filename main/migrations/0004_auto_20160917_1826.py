# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-17 16:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20160917_1824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='employmentBegin',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='employmentEnd',
        ),
    ]
