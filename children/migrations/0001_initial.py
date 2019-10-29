# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-10-25 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Children',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=254)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=6)),
                ('birthday', models.DateField()),
                ('enjoys', models.TextField()),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]