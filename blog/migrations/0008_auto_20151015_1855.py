# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_article_article_alies'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='article_alies',
            new_name='alies',
        ),
    ]
