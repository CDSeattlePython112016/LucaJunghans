# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-16 03:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20161116_0252'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='published',
            field=models.CharField(default=False, max_length=55),
        ),
    ]
