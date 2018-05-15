# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chemical',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('size', models.CharField(verbose_name='规格', max_length=32, blank=True, null=True)),
                ('number', models.IntegerField(verbose_name='数量', default=1)),
                ('public_or_private', models.CharField(verbose_name='公用/私人', max_length=4, default='0', choices=[('0', '公用'), ('1', '私有')])),
                ('entry_time', models.DateField(verbose_name='入库时间', auto_now_add=True)),
                ('notes', models.TextField(verbose_name='备注', blank=True, null=True)),
            ],
            options={
                'verbose_name': '药品列表',
                'verbose_name_plural': '药品列表',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ChemicalsMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('CAS', models.CharField(verbose_name='CAS号', max_length=32, unique=True)),
                ('chinese_name', models.CharField(verbose_name='中文名称', max_length=64, blank=True)),
                ('english_name', models.CharField(verbose_name='英文名称', max_length=64, blank=True, null=True)),
                ('chemical_formula', models.CharField(verbose_name='化学式', max_length=64, blank=True, null=True)),
                ('details', models.TextField(verbose_name='详细信息', blank=True, null=True)),
            ],
            options={
                'verbose_name': '药品信息',
                'verbose_name_plural': '药品信息',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('location', models.CharField(verbose_name='存储位置', max_length=32, unique=True)),
                ('details', models.TextField(verbose_name='详细信息', blank=True, null=True)),
            ],
            options={
                'verbose_name': '位置信息',
                'verbose_name_plural': '位置信息',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='姓名', max_length=32, unique=True)),
                ('contact', models.CharField(verbose_name='联系方式', max_length=32, blank=True, null=True)),
            ],
            options={
                'verbose_name': '人员',
                'verbose_name_plural': '人员',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('person_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='chemicals.Person')),
            ],
            options={
                'verbose_name': '老师/职工',
                'verbose_name_plural': '老师/职工',
                'ordering': ['id'],
            },
            bases=('chemicals.person',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('person_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='chemicals.Person')),
            ],
            options={
                'verbose_name': '学生',
                'verbose_name_plural': '学生',
                'ordering': ['name'],
            },
            bases=('chemicals.person',),
        ),
        migrations.AddField(
            model_name='location',
            name='responsible_man',
            field=models.ForeignKey(verbose_name='柜子负责人', blank=True, null=True, to='chemicals.Person'),
        ),
        migrations.AddField(
            model_name='chemical',
            name='chemical',
            field=models.ForeignKey(verbose_name='药品名称', to='chemicals.ChemicalsMessage'),
        ),
        migrations.AddField(
            model_name='chemical',
            name='location',
            field=models.ForeignKey(verbose_name='存储位置', blank=True, null=True, to='chemicals.Location'),
        ),
        migrations.AddField(
            model_name='chemical',
            name='purchaser',
            field=models.ForeignKey(verbose_name='购买人', blank=True, null=True, related_name='purchaser', to='chemicals.Person'),
        ),
        migrations.AddField(
            model_name='chemical',
            name='responsible_man',
            field=models.ForeignKey(verbose_name='负责人', blank=True, null=True, related_name='responsible_man', to='chemicals.Person'),
        ),
        migrations.AddField(
            model_name='chemical',
            name='approver',
            field=models.ForeignKey(verbose_name='审批人', blank=True, null=True, related_name='approver', to='chemicals.Staff'),
        ),
    ]
