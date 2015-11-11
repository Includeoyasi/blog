# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20151014_2107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='article_url',
            new_name='alias',
        ),
        migrations.RenameField(
            model_name='heading',
            old_name='heading_url',
            new_name='alias',
        ),
    ]
