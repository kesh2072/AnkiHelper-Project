from django.shortcuts import render
from django.http import JsonResponse
from .anki_utils import get_decks, get_card_info, open_anki, is_anki_open
import os
import requests
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

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

@api_view(['GET'])
def get_deck_cards(request, deck_name):
    find_res = requests.post("http://127.0.0.1:8765", json={
        "action": "findCards",
        "version": 6,
        "params": {"query": f'deck:"{deck_name}"'}
    }).json()

    card_ids = find_res.get("result", [])

    info_res = requests.post("http://127.0.0.1:8765", json={
        "action": "cardsInfo",
        "version": 6,
        "params": {"cards": card_ids}
    }).json()
    print(info_res.get("result", []))

    return Response(info_res.get("result", []))

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_note_to_deck(request):
    front = request.data.get("front_text")
    back = request.data.get("back_text")
    tags = request.data.get("tags", [""])

    if not front:
        return Response({"error": "front text is required"}, status=400)
    
    response = requests.post(
        "http://localhost:8765", json={
            "action": "addNote",
            "version": 5,
            "params": {
                "note": {
                    "deckName": "TestDeck",
                    "modelName": "Basic",
                    "fields": {
                        "Front": front,
                        "Back": back,
                    },
                    "tags": tags or [""]
                }
            }
        }
    )
    
    try:
        data = response.json()
    except Exception:
        data = {"error": "Trouble connecting to AnkiConnect", "raw": response.text}

    return Response(data)