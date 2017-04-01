# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviewer', '0007_remove_reportsnapshot_report_submitted_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportsnapshot',
            name='YYYYMM',
            field=models.CharField(default=b'', max_length=6),
        ),
    ]
