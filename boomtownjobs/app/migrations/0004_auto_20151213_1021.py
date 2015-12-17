# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20151212_1645'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TestClass',
        ),
        migrations.AddField(
            model_name='company',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, default='+12069371234'),
        ),
    ]
