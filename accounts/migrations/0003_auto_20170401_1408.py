# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 08:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20170401_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploaddata',
            name='debit_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.DebitCategory'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uploaddata',
            name='upload_time',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 4, 1, 14, 8, 29, 700000)),
            preserve_default=False,
        ),
    ]
