# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviewer', '0005_auto_20170328_0550'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportsnapshot',
            name='report_submitted_by',
            field=models.CharField(default=b'', max_length=20),
        ),
    ]
