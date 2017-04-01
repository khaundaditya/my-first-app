# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_auto_20170328_0621'),
    ]

    operations = [
        migrations.AddField(
            model_name='digitalliteracyreport',
            name='user_name',
            field=models.CharField(default=b'', max_length=20),
        ),
        migrations.AddField(
            model_name='hardwarereport',
            name='user_name',
            field=models.CharField(default=b'', max_length=20),
        ),
        migrations.AddField(
            model_name='nofnreport',
            name='user_name',
            field=models.CharField(default=b'', max_length=20),
        ),
        migrations.AddField(
            model_name='softwarereport',
            name='user_name',
            field=models.CharField(default=b'', max_length=20),
        ),
        migrations.AddField(
            model_name='swanreport',
            name='user_name',
            field=models.CharField(default=b'', max_length=20),
        ),
    ]
