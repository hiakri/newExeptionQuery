# -*-coding:utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'home.html')


def upload(request):
    return render(request, 'upload.html')


def exception_query(request):
    return render(request, 'exceptionQuery.html')


def show(request):
    return render(request, 'show.html')