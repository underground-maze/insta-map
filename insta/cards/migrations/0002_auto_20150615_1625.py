# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import helpers.service
import django.utils.timezone
import helpers.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='YoutubeLogger',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('upload_at', models.DateTimeField(verbose_name='Дата загрузки', default=django.utils.timezone.now)),
                ('status', models.PositiveSmallIntegerField(verbose_name='Состояние загрузки', choices=[(0, 'SUCCESS'), (1, 'ERROR')])),
                ('description', models.TextField(verbose_name='Описание')),
                ('card', models.ForeignKey(to='cards.Card', verbose_name='Карточка')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='card',
            name='video',
            field=models.FileField(null=True, verbose_name='Видеофайл', validators=[helpers.validators.validate_video], blank=True, upload_to=helpers.service.video_path),
        ),
    ]
