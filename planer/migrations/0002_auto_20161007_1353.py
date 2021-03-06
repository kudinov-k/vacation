# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-10-07 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planer', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='plan',
            options={'verbose_name': '\u043f\u043b\u0430\u043d', 'verbose_name_plural': '\u043f\u043b\u0430\u043d\u044b'},
        ),
        migrations.AlterField(
            model_name='plan',
            name='cash',
            field=models.IntegerField(verbose_name='\u043d\u0430\u043b\u0438\u0447\u043d\u044b\u0435'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='destination',
            field=models.TextField(verbose_name='\u043a\u0443\u0434\u0430'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='end_date',
            field=models.DateField(verbose_name='\u043a\u043e\u043d\u0435\u0446'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='start_date',
            field=models.DateField(verbose_name='\u043d\u0430\u0447\u0430\u043b\u043e'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='title',
            field=models.CharField(max_length=150, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
    ]
