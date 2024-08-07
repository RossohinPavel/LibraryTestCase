from django.shortcuts import render
from books.views import books_list


# Create your views here.
def index(request):
	if not request.user.is_authenticated:
		return render(request, 'nav.html', context={'title': 'Библиотека'})
	return books_list(request)
