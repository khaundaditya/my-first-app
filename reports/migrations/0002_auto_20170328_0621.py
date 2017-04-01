# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cscreport',
            name='user_name',
            field=models.CharField(default=b'', max_length=20),
        ),
        migrations.AddField(
            model_name='manpowerreport',
            name='user_name',
            field=models.CharField(default=b'', max_length=20),
        ),
    ]
