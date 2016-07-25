# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-20 13:59
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cityscore', '0013_auto_20160714_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='cityname',
            field=models.CharField(max_length=200, verbose_name='City name'),
        ),
        migrations.AlterField(
            model_name='city',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='metric',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cityscore.City', verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='metric',
            name='definition',
            field=models.CharField(max_length=200, verbose_name='Definition of metric'),
        ),
        migrations.AlterField(
            model_name='metric',
            name='direction',
            field=models.BooleanField(default=1, verbose_name='Check this box if an improvement in the metric is indicated by it going up (e.g., smiles). Leave it unchecked in the opposite case (e.g., frowns).'),
        ),
        migrations.AlterField(
            model_name='metric',
            name='historic',
            field=models.BooleanField(default=0, verbose_name="Check the box if you lack a target for this metric. If checked, we will not be able to generate truly accurate scores for this metric without at least a quarter of data, but after at least 90 data values are entered we can automatically calculate a moving target that is responsive to your city's historic performance."),
        ),
        migrations.AlterField(
            model_name='metric',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Metric name'),
        ),
        migrations.AlterField(
            model_name='metric',
            name='target',
            field=models.FloatField(verbose_name='What is the target value? If this metric is historic (i.e., the above is checked), give an estimate for an average value you expect for this metric or a pre-existing historical average, and we will pick up calculations once we have enough data. (This can be changed later!)'),
        ),
        migrations.AlterField(
            model_name='metric',
            name='trend',
            field=models.BooleanField(default=0, verbose_name='Check this box if this metric is measured on a long-term basis (ex. homicides). This means that there may be days where the value is zero, for which the score is not relevant.'),
        ),
        migrations.AlterField(
            model_name='value',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cityscore.City', verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='value',
            name='entry_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='value',
            name='metric',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cityscore.Metric', verbose_name='Metric'),
        ),
        migrations.AlterField(
            model_name='value',
            name='val',
            field=models.FloatField(verbose_name='Value'),
        ),
    ]
