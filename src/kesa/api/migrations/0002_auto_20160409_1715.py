# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-09 17:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='graph',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Graph'),
        ),
    ]