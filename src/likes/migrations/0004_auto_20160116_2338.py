# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('likes', '0003_auto_20160116_2258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='user_liked',
        ),
        migrations.AddField(
            model_name='like',
            name='liked_users',
            field=models.ManyToManyField(related_name='liked_users', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.OneToOneField(related_name='liker', to=settings.AUTH_USER_MODEL),
        ),
    ]
