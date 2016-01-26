# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=models.CharField(unique=True, max_length=120, default=datetime.datetime(2016, 1, 15, 17, 9, 35, 869104, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
