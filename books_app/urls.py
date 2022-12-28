from django.urls import path

from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    path('', BookListView.as_view(), name='books-list'),
    path('<int:id>/', BookDetailView.as_view(), name='books-detail'),
    path('create/', BookCreateView.as_view(), name='books-create'),
    path('<int:id>/update/', BookUpdateView.as_view(), name='books-update'),
    path('<int:id>/delete/', BookDeleteView.as_view(), name='books-delete'),
]
