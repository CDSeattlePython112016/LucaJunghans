# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-16 02:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20161115_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='review',
            field=models.CharField(default=False, max_length=2000),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=55),
        ),
    ]