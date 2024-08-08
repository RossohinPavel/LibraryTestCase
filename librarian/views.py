from django.shortcuts import render
from django.contrib.auth.decorators import login_required

context = {
	'title': 'Список должников',
	'links': {'Список должников': 'home'}
}


# Create your views here.
@login_required
def debtors_list(request):
	"""Представление для отображения списка книг"""
	return render(request, 'librarian/debtors.html', context=context)
