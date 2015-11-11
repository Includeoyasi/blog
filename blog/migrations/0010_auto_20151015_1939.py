# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_heading_alies'),
    ]

    operations = [
        migrations.RenameField(
            model_name='heading',
            old_name='alies',
            new_name='alies_heading',
        ),
    ]
