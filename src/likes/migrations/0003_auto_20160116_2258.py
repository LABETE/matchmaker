# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0002_auto_20160116_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.OneToOneField(related_name='my_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
