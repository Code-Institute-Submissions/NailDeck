# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-30 18:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20200730_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=254),
        ),
    ]
