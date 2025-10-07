from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("api/book/", views.view_book_api, name="view_book_api"),
]
