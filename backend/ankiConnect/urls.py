from django.urls import path
from . import views

urlpatterns = [
    path("api/anki/", views.view_decks, name="get_anki_decks"),
    path("api/ankicard", views.view_cards, name="view cards"),
    path("api/deck/<str:deck_name>/", views.get_deck_cards),
]