# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-11-01 12:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20191031_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='full_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]