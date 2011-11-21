from django.conf.urls.defaults import patterns, include, url
from views import confuse 

urlpatterns = patterns('',
  url(r'^api/(?P<domainname>[^/]*)/$',confuse, name='pageview'),
