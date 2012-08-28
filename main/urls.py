# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('main.views',
    url(r'^$', 'main_view', name='main'),
)
