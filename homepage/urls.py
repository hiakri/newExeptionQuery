# -*-coding:utf-8 -*-
from django.conf.urls import url
from homepage.views import index,upload,exception_query,show

urlpatterns = [

    url(r'^index/$', index, name='index'),

    url(r'^EImport/upload/$', upload, name='upload'),
    url(r'^EQuery/exceptionquery/$', exception_query, name='exceptionquery'),
    url(r'^EShow/show/$', show, name='show'),


]
