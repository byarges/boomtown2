# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20151213_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='email',
            field=models.EmailField(default='humanresources@fakeemail.com', max_length=254),
        ),
    ]
