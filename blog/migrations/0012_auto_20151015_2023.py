# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20151015_1940'),
    ]

    operations = [
        migrations.RenameField(
            model_name='heading',
            old_name='alies',
            new_name='heading_alies',
        ),
    ]
