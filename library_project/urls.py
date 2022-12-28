"""library_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse, HttpRequest
from django.views.generic import TemplateView


def response_error_handler(request: HttpRequest, exception=None) -> HttpResponse:
    return HttpResponse('Now we have an error handler content!!!', status=404)


handler = response_error_handler

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('admin/', admin.site.urls),
    path('books/', include('books_app.urls')),
    path('users/', include('users_app.urls')),

    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api_app.urls')),
    path('', include('api_app.urls')),

    # path('', TemplateView.as_view(template_name='index.html')),
    path('', TemplateView.as_view(template_name='about.html')),
]
