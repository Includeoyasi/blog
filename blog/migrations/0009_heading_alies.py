# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20151015_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='heading',
            name='alies',
            field=models.CharField(max_length=70, null=True, blank=True),
        ),
    ]
