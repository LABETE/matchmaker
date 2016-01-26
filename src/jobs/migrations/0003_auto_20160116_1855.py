# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20160116_1844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employermatch',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='locationmatch',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='positionmatch',
            name='slug',
        ),
        migrations.AddField(
            model_name='employer',
            name='slug',
            field=models.CharField(max_length=220, default='abc', unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='slug',
            field=models.CharField(max_length=220, default='abc', unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='slug',
            field=models.CharField(max_length=220, default='abc', unique=True),
            preserve_default=False,
        ),
    ]
