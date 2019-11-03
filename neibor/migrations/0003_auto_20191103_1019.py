# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-03 10:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neibor', '0002_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='neighborhood',
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neibor.Neighborhood'),
        ),
    ]
