# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-22 17:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_mentor'),
        ('TeamMap', '0006_auto_20180822_1719'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Student')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TeamMap.Team')),
            ],
        ),
        migrations.RemoveField(
            model_name='teamuser',
            name='team',
        ),
        migrations.RemoveField(
            model_name='teamuser',
            name='user',
        ),
        migrations.DeleteModel(
            name='TeamUser',
        ),
    ]
