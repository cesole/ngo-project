# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-11-04 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_auto_20191104_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank='True', upload_to='images'),
        ),
    ]