

# Create your views here.
from django.http import HttpResponse, JsonResponse
from books.models import Books
from django.template import Context, loader
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def index(request):
      books_list = Books.objects.all() 
      t = loader.get_template('books/index.html')
      c = Context({'books_list': books_list,})
      return HttpResponse(t.render(c))

def books(request, books):
    b = Books.objects.filter(title = books).first()
    return render(request, 'books/book_info.html', {'b': b})

def search(request):
    return render(request, 'books/search.html')

@csrf_exempt
def search_info(request):
    post = request.POST
    data = {}
    if not post['term'].isspace():
        data['response'] = list(Books.objects.filter(title__istartswith = post['term']).values())
    return JsonResponse(data)

