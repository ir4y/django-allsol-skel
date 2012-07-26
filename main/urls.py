# -*- coding: utf-8 -*-
__author__ = 'jackdevil'

from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('main.views',
    url(r'^$', 'main_view', name='main'),
)