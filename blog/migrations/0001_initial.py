# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('article_title', models.CharField(max_length=165)),
                ('article_text', ckeditor.fields.RichTextField(max_length=10000)),
                ('article_date', models.DateTimeField(verbose_name=b'date published')),
                ('article_img', models.ImageField(default=0, upload_to=b'')),
                ('article_likes', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='Heading',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('heading_title', models.TextField(verbose_name=b'add heading')),
            ],
            options={
                'db_table': 'heading',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='article_heading',
            field=models.ForeignKey(to='blog.Heading'),
        ),
    ]
