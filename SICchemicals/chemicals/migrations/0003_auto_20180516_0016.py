# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chemicals', '0002_auto_20180516_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chemical',
            name='size',
            field=models.CharField(verbose_name='规格', max_length=8, blank=True, null=True),
        ),
    ]
