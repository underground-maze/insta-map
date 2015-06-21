# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import helpers.service
import geoposition.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('position', geoposition.fields.GeopositionField(max_length=42, verbose_name='Координаты')),
                ('video', models.FileField(upload_to=helpers.service.video_path, verbose_name='Видеофайл')),
                ('youtube_id', models.CharField(blank=True, max_length=32, verbose_name='ID видео на youtube', null=True)),
                ('description', models.TextField(blank=True, verbose_name='Описание', null=True)),
                ('radius', models.PositiveSmallIntegerField(default=10, verbose_name='Радиус (км)')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата добавления')),
                ('checked_at', models.DateTimeField(blank=True, verbose_name='Дата проверки', null=True)),
                ('status', models.CharField(default='new', max_length=10, verbose_name='Статус', choices=[('new', 'Не проверено'), ('accepted', 'Принято'), ('rejected', 'Отклонено')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'ordering': ('-created_at',),
                'verbose_name': 'карточка',
                'verbose_name_plural': 'карточки',
            },
            bases=(models.Model,),
        ),
    ]
