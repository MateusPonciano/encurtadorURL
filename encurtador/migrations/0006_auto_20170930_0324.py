# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 03:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encurtador', '0005_auto_20170929_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='code',
            field=models.CharField(default='0', max_length=100, unique=True),
        ),
    ]
