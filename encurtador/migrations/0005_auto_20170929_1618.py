# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 16:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encurtador', '0004_auto_20170929_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='code',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]