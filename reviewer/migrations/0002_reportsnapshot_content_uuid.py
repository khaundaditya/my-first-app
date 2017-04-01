# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('reviewer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportsnapshot',
            name='content_uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True, editable=False),
        ),
    ]
