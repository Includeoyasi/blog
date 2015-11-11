# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20151015_1723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='alias',
        ),
        migrations.RemoveField(
            model_name='heading',
            name='alias',
        ),
    ]
