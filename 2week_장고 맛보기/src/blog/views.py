from django.shortcuts import render
from django.http import HttpResponse
from random import randint
from .models import Article


def index(request):
    article_list = Article.objects.all()
    context={
        'article_list':article_list
    }
    return render(request,'index.html',context)

    
