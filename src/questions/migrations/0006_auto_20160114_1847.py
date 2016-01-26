# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_auto_20160114_0413'),
    ]

    operations = [
        migrations.AddField(
            model_name='useranswer',
            name='my_points',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='useranswer',
            name='their_pints',
            field=models.IntegerField(default=-1),
        ),
    ]
