# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20151015_2023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag_title', models.TextField(verbose_name=b'add tag')),
                ('tag_alies', models.CharField(max_length=70, null=True, blank=True)),
            ],
            options={
                'db_table': 'tag',
            },
        ),
    ]
