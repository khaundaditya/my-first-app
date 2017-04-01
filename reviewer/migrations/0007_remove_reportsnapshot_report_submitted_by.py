# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviewer', '0006_reportsnapshot_report_submitted_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportsnapshot',
            name='report_submitted_by',
        ),
    ]
