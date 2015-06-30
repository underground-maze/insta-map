# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_auto_20150615_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='radius',
            field=models.PositiveSmallIntegerField(default=5, verbose_name='Радиус (км)'),
        ),
    ]
