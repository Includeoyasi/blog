# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20151015_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_alies',
            field=models.CharField(max_length=70, null=True, blank=True),
        ),
    ]
