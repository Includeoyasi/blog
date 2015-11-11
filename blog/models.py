# -*- coding: utf-8 -*-

from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Heading(models.Model):
    class Meta():
        db_table = 'heading'
    
    heading_title = models.TextField(verbose_name="add heading")
    heading_alies = models.CharField(max_length=70,null=True, blank=True, help_text='url')

    def __unicode__(self):
        return self.heading_title

class Tag(models.Model):
    class Meta():
        db_table = 'tag'
    
    tag_title = models.TextField(verbose_name="add tag")
    tag_alies = models.CharField(max_length=70,null=True, blank=True, help_text='url')

    def __unicode__(self):
        return self.tag_title
    
class Article(models.Model):
    class Meta():
        db_table = 'article'
        ordering = ['-article_date']

    article_title = models.CharField(max_length=165, help_text='Название статьи')
    article_text = RichTextField(max_length=10000)
    article_date = models.DateTimeField('date published')
    article_img = models.ImageField(null=True, blank=True, help_text='Миниатюра')
    article_likes = models.IntegerField(default=0)
    article_heading = models.ForeignKey(Heading)
    alies = models.CharField(max_length=70,null=True, blank=True, help_text='url')
    tags = models.ManyToManyField(Tag)
    page_title = models.CharField(max_length=60,null=True, blank=True)
    page_description = models.CharField(max_length=160,null=True, blank=True)