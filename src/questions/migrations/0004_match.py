# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0003_useranswer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('match_decimal', models.DecimalField(default=0.0, decimal_places=8, max_digits=16)),
                ('questions_answered', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user_a', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='match_user_a')),
                ('user_b', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='match_user_b')),
            ],
        ),
    ]
