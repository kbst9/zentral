# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-22 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20151222_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='osversion',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='systeminfo',
            name='computer_name',
            field=models.TextField(blank=True, null=True),
        ),
    ]