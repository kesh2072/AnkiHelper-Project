from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("api/book/", views.view_book_api, name="view_book_api"),
    path('save/', views.save_article, name='save_article'),
    path('saved/', views.list_saved_articles, name='list_saved_articles'),
]
