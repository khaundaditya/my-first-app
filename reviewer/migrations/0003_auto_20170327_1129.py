# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('reviewer', '0002_reportsnapshot_content_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.AddField(
            model_name='comment',
            name='snapshot_id',
            field=models.UUIDField(default=uuid.uuid4, unique=True, editable=False),
        ),
    ]
