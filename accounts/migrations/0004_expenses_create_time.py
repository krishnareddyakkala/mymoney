# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 15:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20170401_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenses',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
