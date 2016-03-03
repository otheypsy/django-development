# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-02 09:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('desai', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='skill_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='skilldetail',
            name='detail_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='skilldetail',
            name='detail_description',
            field=models.TextField(max_length=500),
        ),
    ]