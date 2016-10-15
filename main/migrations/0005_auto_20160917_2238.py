# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-17 20:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20160917_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='active',
            field=models.BooleanField(default=True, verbose_name='aktiv?'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='firstName',
            field=models.CharField(max_length=30, verbose_name='Vorname'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='lastName',
            field=models.CharField(max_length=30, verbose_name='Nachname'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='number',
            field=models.PositiveSmallIntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Personalnummer'),
        ),
    ]
