

# Create your views here.

from django.http import HttpResponse, JsonResponse
from movies.models import Movies
from django.template import Context, loader
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def index(request):
      movies_list = Movies.objects.all() 
      t = loader.get_template('movies/inde.html')
      c = Context({'movies_list': movies_list,})
      return HttpResponse(t.render(c))

def movies(request, movies):
    m = Movies.objects.filter(title = movies).first()
    return render(request, 'movies/movie_info.html', {'m': m})

def search(request):
    return render(request, 'movies/search.html')

@csrf_exempt
def search_info(request):
    post = request.POST
    data = {}
    if not post['term'].isspace():
        data['response'] = list(Movies.objects.filter(title__istartswith = post['term']).values())
    return JsonResponse(data)



