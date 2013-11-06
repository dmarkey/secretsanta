__author__ = 'dmarkey'
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'app.views.launch', name='launch'),
    url(r'^(\w*)$', 'app.views.manage', name='manage'),
)
