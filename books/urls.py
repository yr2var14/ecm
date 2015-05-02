from django.conf.urls import patterns, url
from books import views

urlpatterns = patterns('',
    url(r'^$', views.index, name = 'index'),
    url(r'^book=(?P<books>\w+)/$', views.books, name='books'),
    url(r'^search_info/$', views.search_info, name = 'search_info'),
    url(r'^search/$', views.search, name = 'search'),
 
 
)
