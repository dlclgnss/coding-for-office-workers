from django.shortcuts import render
from django.http import HttpResponse
from random import randint


def index(request):
    context:{

    }

    return render(request,'index.html',context)