# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-15 00:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20160409_1716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='roomID',
        ),
    ]