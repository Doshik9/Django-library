from rest_framework import viewsets, mixins, response
from rest_framework.decorators import action
from django.contrib.auth.models import User

from books_app.models import Book, UserBook

from .serializers import BookSerializer, UserSerializer, UserBookSerializer

# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(methods=['get'], detail=False, url_path='novelties')
    def novelties(self, request):
        books = (
            Book.objects
            .filter(publication_date__year=2022)
        )
        serializer = BookSerializer(books, many=True)
        return response.Response(data=serializer.data)


class UserViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserBookViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = UserBook.objects.all()
    serializer_class = UserBookSerializer
