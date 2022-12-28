from rest_framework import serializers
from django.contrib.auth.models import User

from books_app.models import Book, UserBook

# Create your serializers here.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['book_name', 'author', 'genre_type_id', 'publisher', 'publication_date']


class UserBookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserBook
        fields = ['reader', 'book', 'issue_date', 'return_date']


class UserBookTextSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = UserBook
        fields = ['book', 'issue_date', 'return_date']


class UserSerializer(serializers.ModelSerializer):
    readers = UserBookTextSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'readers']
