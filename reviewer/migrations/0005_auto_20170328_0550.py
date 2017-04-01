# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviewer', '0004_auto_20170327_1226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='snapshot_id',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(related_name='comments', default=b'', to='reviewer.ReportSnapShot'),
        ),
    ]
