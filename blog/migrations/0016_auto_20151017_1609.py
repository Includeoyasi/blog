# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20151017_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_img',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
    ]
