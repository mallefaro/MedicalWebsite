# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basecustomuser',
            name='middle_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='middle name'),
        ),
    ]
