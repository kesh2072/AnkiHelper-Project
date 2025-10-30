from django.shortcuts import render
from django.http import JsonResponse
from .anki_utils import get_decks, get_card_info, open_anki, is_anki_open
import os
import requests
from users.models import Word, UserWord
from django.contrib.auth.models import User
from datetime import date

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

def store_words(request):
    """
    This is hardcoded in, but most of this will be re-useable later
    What this function does is:
    - Finds all of the card ids in a given Anki deck
    - Searches through all these ids to get the card info (and strips it down to get the actual word)
    - Uploads these words to the user's UserWord database, so we can search these words against the stored articles

    To change this later, I just need to:
    - change deck name to not be hardcoded
    - just use request.user instead of default user
    - find a more flexible way to extract the word from Anki deck (all of the templates seem to change slightly)
    """
    deck_name = "test"
    response = requests.post(
        "http://127.0.0.1:8765",
        json={"action": "findCards", "params": {"query": f"deck:{deck_name}"}, "version": 6}
    )

    card_ids = response.json()["result"]

    response = requests.post(
        "http://127.0.0.1:8765",
        json={"action": "cardsInfo", "params": {"cards": card_ids}, "version": 6}
    )

    cards = response.json()["result"]

    word = cards[0]['fields'].get("Word").get('value')

    words = []

    for item in cards:
        words.append(item['fields'].get('Word').get('value'))

    user = User.objects.first()
    for word in words:
        word_obj, created = Word.objects.get_or_create(word=word)

        UserWord.objects.get_or_create(user=user, word=word_obj, due_date=date.today(), known=False)
    
    print("Finished uploading words to database")

    print(UserWord.objects.all())
