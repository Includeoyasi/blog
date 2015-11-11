# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_article_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='page_description',
            field=models.CharField(max_length=160, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='page_title',
            field=models.CharField(max_length=60, null=True, blank=True),
        ),
    ]
