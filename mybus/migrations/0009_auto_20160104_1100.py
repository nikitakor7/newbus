# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-04 05:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mybus', '0008_auto_20160104_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businfo',
            name='is_public',
            field=models.BooleanField(default=True, verbose_name=b'Like My Service?'),
        ),
    ]