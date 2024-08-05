from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.
class Book(models.Model):
	"""Модель книги"""

	title = models.CharField(max_length=255)
	author = models.CharField(max_length=100)
	genre = models.CharField(max_length=100)

	# Связка с читателем
	# reader = models.ForeignKey()
	
	# Отслеживание изменений
	history = HistoricalRecords()

	def __str__(self) -> str:
		return f'{self.title} - {self.author}'
