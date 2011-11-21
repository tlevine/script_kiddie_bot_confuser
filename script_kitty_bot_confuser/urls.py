from django.conf.urls.defaults import patterns, include, url
from views import confuse 

#Confuse bots on these URLs
urlpatterns = patterns('',
  #Languages
  url(r'.php$',confuse),
  url(r'.cgi$',confuse),
  url(r'.rb$',confuse),
  url(r'.aspx$',confuse),
  url(r'.do$',confuse),
  url(r'$',confuse),

  #Version control
  url(r'^.svn',confuse),
  url(r'^.git',confuse),
  url(r'^.hg',confuse),

  #Administration software
  url(r'$',confuse),
)
