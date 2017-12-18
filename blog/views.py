# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models

def index(request):
    # article = models.Article.objects.get(pk=1)
    articles = models.Article.objects.all()
    return render(request, 'index.html', {
        'articles': articles
    })

def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'article_page.html', {'article': article})

def edit_page(request, article_id):
    if str(article_id) == '0':  # 新建文章
        return render(request, 'edit_page.html')

    # 修改文章
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'edit_page.html', {'article': article})


def edit_action(request):
    title = request.POST.get('title', 'Title')  # Title是给一个默认值
    content = request.POST.get('content', 'Content')  # Content是给一个默认值
    article_id = request.POST.get('article_id', '0')  # Content是给一个默认值

    if article_id == '0':   # 新建文章
        models.Article.objects.create(title=title, content=content)
        return HttpResponseRedirect('/blog/index/')

    # 修改文章
    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    return HttpResponseRedirect('/blog/index/')

