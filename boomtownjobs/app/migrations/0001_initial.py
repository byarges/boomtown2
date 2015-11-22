# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('state', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('skill', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='location',
            field=models.ForeignKey(to='app.Location'),
        ),
        migrations.AddField(
            model_name='company',
            name='skill',
            field=models.ForeignKey(to='app.Skill'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='location',
            field=models.ForeignKey(to='app.Location'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='skill',
            field=models.ForeignKey(to='app.Skill'),
        ),
    ]
