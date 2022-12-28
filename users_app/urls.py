from django.urls import path

from .views import (
    UserListView,
    UserDetailView
)

urlpatterns = [
    path('', UserListView.as_view(), name='users-list'),
    path('<int:id>/', UserDetailView.as_view(), name='users-detail'),
]