# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-27 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_star', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='5', max_length=11)),
                ('review_message', models.CharField(max_length=1024)),
            ],
        ),
    ]
