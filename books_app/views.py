from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import BookForm
from .models import Book
from django.views.generic import (
    ListView, DetailView, DeleteView, CreateView, UpdateView
)

# Create your views here.


class BookListView(ListView):
    model = Book
    # Дальше только для удобства
    template_name = 'books_app/book_list.html'
    context_object_name = "books"


class BookDetailView(DetailView):
    model = Book
    # Дальше только для удобства
    template_name = 'books_app/book_detail.html'
    context_object_name = "book"
    pk_url_kwarg = 'id'


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('books-list')
    # Для удобства
    template_name_suffix = '_create'


class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('books-list')
    # Для удобства
    template_name_suffix = '_delete'
    pk_url_kwarg = 'id'


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('books-list')
    # Для удобства
    template_name_suffix = '_update'
    pk_url_kwarg = 'id'


