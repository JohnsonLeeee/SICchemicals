# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chemicals', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chemical',
            options={'verbose_name': '药品列表', 'verbose_name_plural': '药品列表', 'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name': '存储位置信息', 'verbose_name_plural': '存储位置信息', 'ordering': ['id']},
        ),
        migrations.RenameField(
            model_name='chemical',
            old_name='notes',
            new_name='details',
        ),
        migrations.RemoveField(
            model_name='chemical',
            name='chemical',
        ),
        migrations.RemoveField(
            model_name='location',
            name='responsible_man',
        ),
        migrations.AddField(
            model_name='chemical',
            name='CAS',
            field=models.CharField(verbose_name='CAS号', max_length=32, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chemical',
            name='chemical_formula',
            field=models.CharField(verbose_name='化学式', max_length=64, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chemical',
            name='name',
            field=models.CharField(verbose_name='名称', max_length=64, default='lv'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chemical',
            name='public_or_private',
            field=models.CharField(verbose_name='公用/私人', max_length=4, default='0', choices=[('0', '公用'), ('1', '私用')]),
        ),
        migrations.DeleteModel(
            name='ChemicalsMessage',
        ),
    ]
