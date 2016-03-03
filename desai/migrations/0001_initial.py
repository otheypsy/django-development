# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-02 09:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=200)),
                ('skill_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='SkillDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail_name', models.CharField(max_length=200)),
                ('detail_description', models.CharField(max_length=500)),
                ('detail_date', models.DateTimeField(verbose_name='date published')),
                ('skill_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='desai.Skill')),
            ],
        ),
    ]