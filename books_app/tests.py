from django.test import TestCase

import pytest
from django.urls import reverse

from .models import Book

# Create your tests here.
def test_home_page_accessability(client):

    url = reverse("home")

    response = client.get(url)

    assert response.status_code == 200
    assert "Home page" in response.content.decode("utf-8")


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
def test_books_list(client, books_group):

    url = reverse("books-list")

    response = client.get(url)

    assert response.status_code == 200
    assert "Первая книга" in response.content.decode("utf-8")
    assert "Вторая книга" in response.content.decode("utf-8")
    assert "Третья книга" in response.content.decode("utf-8")


@pytest.mark.django_db
def test_books_detail_one(client, first_book):

    url = reverse("books-detail", args=[1])

    response = client.get(url)

    assert response.status_code == 200
    assert "Первая книга" in response.content.decode("utf-8")


@pytest.mark.django_db
def test_books_detail_two(client, second_book):

    url = reverse("books-detail", args=[1])

    response = client.get(url)

    assert response.status_code == 200
    assert "Вторая книга" in response.content.decode("utf-8")


@pytest.mark.django_db
def test_books_detail_three(client, books_group):

    url = reverse("books-detail", args=[3])

    response = client.get(url)

    assert response.status_code == 200
    assert "Третья книга" in response.content.decode("utf-8")


@pytest.mark.django_db
@pytest.mark.parametrize(
    ["pk", "book_name"],
    [
        [1, "Первая книга"],
        [2, "Вторая книга"],
        [3, "Третья книга"],
    ],
)
def test_works_detail(pk, book_name, client, books_group):

    url = reverse("books-detail", args=[pk])

    response = client.get(url)

    assert response.status_code == 200
    assert book_name in response.content.decode("utf-8")
