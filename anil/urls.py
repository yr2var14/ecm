from django.conf.urls import patterns, include, url
from django.contrib import admin
#from movies import views
#from books import views
from main import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'anil.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name = 'index'),
    url(r'^books/', include('books.urls')),
    url(r'^movies/', include('movies.urls')),
    #url(r'^movies/movie=(?P<movies>\w+)/$', views.movies, name='movies'),
    #url(r'^movies/search_info/$', views.search_info, name = 'search_info'),
    #url(r'^movies/search/$', views.search, name = 'search'),
    #url(r'^books/book=(?P<books>\w+)/$', views.books, name='books'),
    #url(r'^books/search_info/$', views.search_info, name = 'search_info'),
    #url(r'^books/search/$', views.search, name = 'search'),
 
 
    
    
)
