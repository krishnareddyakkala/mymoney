# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 10:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DebitCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=120, unique=True, verbose_name='Category Name')),
            ],
        ),
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('spent_date', models.DateField(verbose_name='Spent on Date')),
                ('amount', models.FloatField(verbose_name='Amount Spent')),
                ('debit_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.DebitCategory')),
            ],
        ),
        migrations.CreateModel(
            name='MainCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=120, unique=True, verbose_name='Category Name')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=120, unique=True, verbose_name='Category Name')),
                ('main_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.MainCategory')),
            ],
        ),
        migrations.AddField(
            model_name='expenses',
            name='main_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.MainCategory'),
        ),
        migrations.AddField(
            model_name='expenses',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.SubCategory'),
        ),
    ]
