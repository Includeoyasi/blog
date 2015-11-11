# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_heading_heading_title2'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_url',
            field=models.CharField(max_length=70, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='heading',
            name='heading_url',
            field=models.CharField(max_length=70, null=True, blank=True),
        ),
    ]
