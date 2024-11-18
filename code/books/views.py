from django.shortcuts import render, get_object_or_404
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def book_detail(request, post_id):
    book = get_object_or_404(request, id=post_id)
    return render(request, 'books/book_detail.html', {'book': book})

