# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PositionMatch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('slug', models.CharField(unique=True, max_length=220)),
                ('hidden', models.BooleanField(default=False)),
                ('liked', models.NullBooleanField()),
                ('job', models.ForeignKey(to='jobs.Job')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='jobmatch',
            name='job',
        ),
        migrations.RemoveField(
            model_name='jobmatch',
            name='user',
        ),
        migrations.AddField(
            model_name='employermatch',
            name='slug',
            field=models.CharField(default='abc', unique=True, max_length=220),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='locationmatch',
            name='slug',
            field=models.CharField(default='abc', unique=True, max_length=220),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='JobMatch',
        ),
    ]
