from django.shortcuts import render
from books.views import books_list
from librarian.views import debtors_list
from django.core.handlers.wsgi import WSGIRequest


# Create your views here.
def index(request: WSGIRequest):
	"""Логика работы главной страницы"""
	if not request.user.is_authenticated:
		return render(request, 'nav.html', context={'title': 'Библиотека'})

	if request.user.is_staff:
		return debtors_list(request)

	return books_list(request)
