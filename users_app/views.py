from books_app.models import UserBook
from django.views.generic import (
    ListView, DetailView
)

# Create your views here.


class UserListView(ListView):
    model = UserBook
    # Дальше только для удобства
    template_name = 'users_app/user_list.html'
    context_object_name = "users"


class UserDetailView(DetailView):
    model = UserBook
    # Дальше только для удобства
    template_name = 'users_app/user_detail.html'
    context_object_name = "user"
    pk_url_kwarg = 'id'





