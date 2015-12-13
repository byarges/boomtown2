# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_testclass'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testclass',
            old_name='name',
            new_name='q',
        ),
    ]
