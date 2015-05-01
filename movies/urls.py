from django.conf.urls import patterns, url
from movies import views

urlpatterns = patterns('',
    url(r'^$', views.index, name = 'index'),
    url(r'^movie=(?P<movies>\w+)/$', views.movies, name='movies'),
    url(r'^search_info/$', views.search_info, name = 'search_info'),
    url(r'^search/$', views.search, name = 'search'),
 
 
    
    
)
