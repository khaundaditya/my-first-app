# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviewer', '0003_auto_20170327_1129'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reportsnapshot',
            unique_together=set([('district', 'owner')]),
        ),
        migrations.RemoveField(
            model_name='reportsnapshot',
            name='created',
        ),
        migrations.RemoveField(
            model_name='reportsnapshot',
            name='today',
        ),
        migrations.RemoveField(
            model_name='reportsnapshot',
            name='updated',
        ),
    ]
