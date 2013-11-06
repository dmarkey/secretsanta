from django.conf.urls import patterns, include, url

from django.contrib import admin
from app import urls
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'secretsanta.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^secretsanta/', include(urls)),
)
