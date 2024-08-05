from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Book


# Register your models here.
admin.site.register(Book, SimpleHistoryAdmin)
