# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-09 16:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('link', models.CharField(max_length=2083)),
                ('description', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'carousel',
                'managed': False,
            },
        ),
    ]
