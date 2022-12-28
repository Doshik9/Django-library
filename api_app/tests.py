from django.test import TestCase

import pytest
from rest_framework.test import APIClient

from books_app.models import Book
# Create your tests here.
@pytest.fixture
def first_book():
    book = Book(book_name="Первая книга")
    book.save()


@pytest.fixture
def second_book():
    book = Book(book_name="Вторая книга")
    book.save()


@pytest.fixture
def third_book():
    book = Book(book_name="Третья книга")
    book.save()


@pytest.fixture
def books_group(
    first_book,
    second_book,
    third_book
):
    pass


@pytest.mark.django_db
def test_books_list_api(books_group):

    client = APIClient()

    response = client.get("/api/books/")

    assert response.status_code == 200
    assert len(response.data) == 3
    assert response.data[0]["book_name"] == "Первая книга"
    assert response.data[1]["book_name"] == "Вторая книга"
    assert response.data[2]["book_name"] == "Третья книга"


@pytest.mark.django_db
def test_books_api_novelties(books_group):

    client = APIClient()

    response = client.get("/api/books/novelties", follow=True)

    assert response.status_code == 200
    assert len(response.data) == 3