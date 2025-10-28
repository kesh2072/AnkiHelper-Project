from django.shortcuts import render
from django.http import JsonResponse
from .anki_utils import get_decks, get_card_info, open_anki, is_anki_open
import os

def view_decks(request):
    open_anki()
    if not is_anki_open():
        return JsonResponse({
            "error": "AnkiConnect not detected. Please make sure Anki is open and the AnkiConnect add-on is installed.",
            "install_url": "https://ankiweb.net/shared/info/2055492159"
        }, status=400)

    data = get_decks()
    print(data)
    print(type(data))
    return JsonResponse(data, safe=False)

def view_cards(request):
    data = get_card_info()
    print(data)
    return JsonResponse(data, safe=False)