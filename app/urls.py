__author__ = 'dmarkey'
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'app.views.launch', name='launch'),
    url(r'(?P<unique_id>.*)', 'app.views.register', name='register'),
)
