# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_auto_20160114_1847'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useranswer',
            old_name='their_pints',
            new_name='their_points',
        ),
    ]
