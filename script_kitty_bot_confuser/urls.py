from django.conf.urls.defaults import patterns, include, url
from views import confuse 

#Confuse bots on these URLs
urlpatterns = patterns('',
  #Other languages
  url(r'.php$',confuse),
  url(r'.cgi$',confuse),
  url(r'.rb$',confuse),
  url(r'.aspx$',confuse),
  url(r'.do$',confuse),
  url(r'.pl$',confuse),

  #Typical directories and files of interest
  url(r'cgi-bin',confuse),
  url(r'^.htaccess',confuse),
  url(r'^.htpasswd',confuse),

  #Version control
  url(r'^.svn',confuse),
  url(r'^.git',confuse),
  url(r'^.hg',confuse),

  #Administration software
  url(r'phpmyadmin',confuse),
  url(r'phpMyAdmin',confuse),
)
