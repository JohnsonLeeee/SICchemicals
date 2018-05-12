# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Chemical',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('CAS', models.CharField(max_length=32)),
                ('chinese_name', models.CharField(max_length=32)),
                ('english_name', models.CharField(max_length=32)),
                ('size', models.CharField(max_length=32)),
                ('num', models.IntegerField(max_length=10)),
                ('location', models.CharField(max_length=32)),
                ('goumairen', models.CharField(max_length=32)),
                ('shenpiren', models.CharField(max_length=32)),
                ('rukutime', models.DateField()),
                ('note', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Chemicals',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('CAS', models.CharField(max_length=32)),
                ('chinese_name', models.CharField(max_length=32)),
                ('english_name', models.CharField(max_length=32)),
                ('details', models.TextField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=32)),
                ('phone', models.CharField(max_length=32)),
            ],
        ),
    ]
