# -*- coding: utf-8 -*-

from django.http.response import HttpResponse, Http404 #обработчики событий
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger #вспомогательные библиотеки
from models import Article, Heading, Tag #импорт моделей
from django.shortcuts import render_to_response, redirect, get_object_or_404 #редитект и его улучшенный аналог
from django.core.context_processors import csrf #защита от  csrf

def articles_category(request, category_alies):
    args = {}
    args.update(csrf(request))
    try:
        heading_id = Heading.objects.get(heading_alies=category_alies)
        args['articles'] = Article.objects.filter(article_heading=heading_id.id)
    except Heading.DoesNotExist:
        try:
            tag_id = Tag.objects.get(tag_alies=category_alies)
            args['articles'] = Article.objects.filter(tags=tag_id.id)
        except Tag.DoesNotExist:
            raise Http404
    args['heading'] = Heading.objects.all()
    return render_to_response('articles.html', args)

# Create your views here.
def articles(request):
    args = {}
    try:
        all_articles = Article.objects.all()
        paginator = Paginator(all_articles, 10)
        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            contacts = paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)

        args['articles'] = contacts
        args['heading'] = Heading.objects.all()
    except Article.DoesNotExist:
        raise Http404
    except Heading.DoesNotExist:
        raise Http404
    return render_to_response('articles.html',  args)

def article(request, alies):
    args = {}
    args.update(csrf(request))
    try:
        args['article'] = Article.objects.get(alies=alies)
    except Article.DoesNotExist:
        raise Http404
    args['heading'] = Heading.objects.all()
    return render_to_response('article.html', args)

def like(request, alies):
    if alies in request.COOKIES:
        redirect('/%s' % alies)
    else:
        article = get_object_or_404(Article, alies=alies)
        article.article_likes += 1
        article.save()
        response = redirect('/%s' % alies)
        response.set_cookie(alies, "like")
        return response
    return redirect('/%s' % alies)