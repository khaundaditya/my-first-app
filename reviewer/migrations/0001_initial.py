# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=80)),
                ('user', models.CharField(default=b'', max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('status', models.CharField(default=b'raised', max_length=12)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='ReportSnapShot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.BinaryField(default=b'')),
                ('owner', models.CharField(max_length=20)),
                ('today', models.CharField(default=b'', max_length=8)),
                ('district', models.CharField(default=b'', max_length=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('report_type', models.CharField(default=b'abc', max_length=20)),
                ('state', models.CharField(default=b'', max_length=20)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='reportsnapshot',
            unique_together=set([('updated', 'district', 'owner')]),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(related_name='comments', to='reviewer.ReportSnapShot'),
        ),
    ]
