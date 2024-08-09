from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Book

common_context = {
	"links": {
		"Список Книг": "home",
		"Мои книги": "mybooks"
	}
	
}

# Create your views here.
class BooksList(LoginRequiredMixin, ListView):
	model = Book
	template_name = 'books/list.html'
	context_object_name = 'books'
	paginate_by = 5
	
	def get_context_data(self, **kwargs):
		context: dict = super().get_context_data(**kwargs)
		context['title'] = 'Список книг'
		context.update(common_context)
		return context


@login_required
def read(request):
	def inner():
		if book.reader is None:
			book.reader = request.user
			return
		if book.reader == request.user:
			book.reader = None
			return

	if request.method == 'POST':
		book = Book.objects.get(pk=request.POST['book_id'])
		inner()
		book.save()

		context = {
			'book': book,
			'user': request.user
		}
	
		return render(request, 'books/list_book_btn.html', context)


@login_required
def mybooks(request):
	"""Представление для отображения списка книг"""
	context = common_context.copy()
	context['title'] = 'Мои книги'
	return render(request, 'books/mybooks.html', context=context)
