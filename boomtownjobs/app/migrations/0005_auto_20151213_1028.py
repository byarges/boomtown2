# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20151213_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='description',
            field=models.CharField(max_length=200, default='"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."'),
        ),
        migrations.AddField(
            model_name='company',
            name='nonvalidatedaddress',
            field=models.CharField(max_length=30, default='1234 99th Ave'),
        ),
    ]
