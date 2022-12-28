from django.urls import path
from rest_framework import routers

from .views import BookViewSet, UserViewSet, UserBookViewSet

router = routers.SimpleRouter()

router.register(r'books', BookViewSet)
router.register(r'users', UserViewSet)
router.register(r'userbook', UserBookViewSet)

urlpatterns = router.urls

# urlpatterns = [
#     path('books/', BookViewSet.as_view({'get': 'list', 'post': 'create'}), name='book-list'),
#     path('books/<int:pk>', BookViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='book-detail'),
#
#     path('users/', UserViewSet.as_view({'get': 'list'}), name='user-list'),
#     path('users/<int:pk>', UserViewSet.as_view({'get': 'retrieve'}), name='user-detail'),
# ]