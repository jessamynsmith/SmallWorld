# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-28 14:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeamMap', '0007_auto_20180822_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='accepting_members',
            field=models.BooleanField(default=True),
        ),
    ]