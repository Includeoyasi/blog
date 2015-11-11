from django.conf.urls import include, url
from django.conf import settings

urlpatterns = [
    url(r'^$', 'blog.views.articles'),
    url(r'^(?P<alies>[-a-zA-Z0-9_]+)$', 'blog.views.article', name="article_detail"),
    url(r'^(?P<category_alies>[-a-zA-Z0-9_]+)/$', 'blog.views.articles_category', name="category"),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^articles/addlike/(?P<alies>[-a-zA-Z0-9_]+)$', 'blog.views.like'),
]
