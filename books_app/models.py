from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Genre(models.TextChoices):
    ROMANCE = 'RM', _('Romance')
    FANTASY = 'FN', _('Fantasy')
    HORROR = 'HR', _('Horror')
    MYSTERY = 'MS', _('Mystery')
    THRILLER = 'TH', _('Thriller')


class Book(models.Model):
    genre_type_id = models.CharField(
        max_length=50,
        choices=Genre.choices,
        default=Genre.ROMANCE,
        help_text='Жанр',
    )
    book_name = models.CharField(
        max_length=50,
        help_text='Название книги'
    )
    author = models.CharField(
        max_length=50,
        help_text='Автор',
    )
    publication_date = models.DateField(
        auto_now_add=True,
        help_text='Дата публикации',
    )
    publisher = models.CharField(
        max_length=50,
        help_text='Издатель',
    )
    readers = models.ManyToManyField(
        User,
        through='UserBook',
        through_fields=('book', 'reader'),
    )


class UserBook(models.Model):
    reader = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='readers',
        help_text='Номер пользователя',
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='user_books',
        help_text='Номер книги',
    )
    issue_date = models.DateTimeField(
        auto_now_add=True,
        help_text='Дата бронирования',
    )
    return_date = models.DateTimeField(
        null=True,
        help_text='Дата возврата',
    )

    class Meta:
        unique_together = ['reader', 'book']