# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviewer', '0008_reportsnapshot_yyyymm'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_to',
            field=models.CharField(default=b'', max_length=20),
        ),
    ]
