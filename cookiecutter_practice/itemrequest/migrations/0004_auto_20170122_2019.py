# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 02:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itemrequest', '0003_auto_20170122_1725'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Unit of Measure')),
                ('abbreviation', models.CharField(max_length=10, verbose_name='Abbreviated UOM')),
            ],
        ),
        migrations.AlterField(
            model_name='itemrequest',
            name='requester',
            field=models.CharField(blank=True, help_text='Name of the person requesting the item', max_length=60),
        ),
    ]
