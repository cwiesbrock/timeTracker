# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-17 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='name',
        ),
        migrations.AddField(
            model_name='employee',
            name='firstName',
            field=models.CharField(default='Firstname', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='lastName',
            field=models.CharField(default='Lastname', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='employmentBegin',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employmentEnd',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='number',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
