# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-02 11:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('desai', '0008_auto_20160302_0520'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skilldetail',
            old_name='skill_id',
            new_name='skill_foreign',
        ),
    ]
