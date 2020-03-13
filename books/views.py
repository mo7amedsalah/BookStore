from django.shortcuts import render
import json
import os
from books.models import Book

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Create your views here.
def index(request):
   
    books = Book.objects.all()
    context = {
        "books": books
    }
    return render(request, "books/index.html", context)


def show(request, book_id):
    context = {}
    

    context["book"] = Book.objects.get(id=book_id)

    return render(request, "books/show.html", context)

