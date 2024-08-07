from django.shortcuts import render
from django.contrib.auth.decorators import login_required

common_context = {
	"links": {
		"Список Книг": "home",
		"Мои книги": "mybooks"
	}
	
}


# Create your views here.
@login_required
def books_list(request):
	"""Представление для отображения списка книг"""
	context = common_context.copy()
	context['title'] = 'Список книг'
	return render(request, 'books/list.html', context=context)


@login_required
def mybooks(request):
	"""Представление для отображения списка книг"""
	context = common_context.copy()
	context['title'] = 'Мои книги'
	return render(request, 'books/mybooks.html', context=context)
