__author__ = 'dmarkey'
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'app.views.launch', name='launch'),
    url(r'(?P<unique_id>\w+)/manageorg', 'app.views.manageorg', name='manageorg'),
    url(r'(?P<unique_id>\w+)/manageuser', 'app.views.manageuser', name='manageuser'),
    url(r'(?P<unique_id>\w+)/', 'app.views.register', name='register'),

)
