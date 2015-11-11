from django.contrib import admin

# Register your models here.
from models import  Article, Heading, Tag

class ArticleinAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['article_title', 'alies', 'article_text', 'article_img', 'article_heading', 'tags']}),
        ('Date information', {'fields': ['article_date']}),
        ('SEO options', {'classes': ('collapse'), 'fields': ('page_title','page_description')}),
    ]
    list_filter = ['article_date', 'article_heading']
    list_display = ('article_title',)

class HeadinginAdmin(admin.ModelAdmin):
	 fields = ['heading_title', 'heading_alies']
	 list_display = ('heading_title',)

class TaginAdmin(admin.ModelAdmin):
     fields = ['tag_title', 'tag_alies']
     list_display = ('tag_title',)

admin.site.register(Article, ArticleinAdmin)
admin.site.register(Heading, HeadinginAdmin)
admin.site.register(Tag, TaginAdmin)