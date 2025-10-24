from django.shortcuts import render
from django.http import JsonResponse
from .anki_utils import get_decks, get_card_info

def view_decks(request):
    data = get_decks()
    return JsonResponse(data, safe=False)

def view_cards(request):
    data = get_card_info()
    print(data)
    return JsonResponse(data, safe=False)