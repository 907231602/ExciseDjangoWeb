from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    print('hello')
    return HttpResponse("hello world!")