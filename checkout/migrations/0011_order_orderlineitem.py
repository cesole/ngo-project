# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-11-01 19:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0010_remove_order_orderlineitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='orderlineitem',
            field=models.ForeignKey(blank='false', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orderlineitem', to='checkout.OrderLineItem'),
        ),
    ]
