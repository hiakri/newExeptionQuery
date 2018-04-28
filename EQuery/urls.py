# -*-coding:utf-8 -*-

from django.conf.urls import url
from homepage.views import index
from EQuery import views


urlpatterns = [

    url(r'^index/$', index, name='index'),
    url(r'^exceptionquery/$', views.exception_query),
    url(r'^query', views.query_result),
    url(r'^upload/$', views.uploadfile, name='import_uploadfile'),
    url(r'^show/$', views.show, name='show'),

]
