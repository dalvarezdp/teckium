# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-12 17:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20170905_2204'),
        ('blogs', '0004_auto_20170912_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Profile'),
        ),
    ]
