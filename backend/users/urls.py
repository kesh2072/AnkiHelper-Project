from django.urls import path
from .views import RegisterUserView
from . import views


urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path("save/", views.save_article),
    path("saved/", views.list_saved_articles),
]