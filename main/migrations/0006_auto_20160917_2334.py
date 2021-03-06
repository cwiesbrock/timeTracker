# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-17 21:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20160917_2238'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('employeeNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='BookingType',
            fields=[
                ('type', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.BookingType'),
        ),
    ]
