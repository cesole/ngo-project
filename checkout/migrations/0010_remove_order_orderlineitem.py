# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-11-01 18:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0009_auto_20191101_1851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='orderlineitem',
        ),
    ]
