import requests
import os
import json

def get_decks():
    decks = requests.post('http://localhost:8765', json={'action': 'deckNames'})
    return decks.json()

def get_card_info():
    card_info = requests.post('http://localhost:8765', json={'action': 'cardsInfo', 'params': {'cards': [1761334419606]}}) # can't get this working without hardcoding it 
    return card_info.text

def get_due_cards():
    due_cards = requests.post('http:localhost:8765', json={'action': 'findCards', 'params': {'query': 'is:due'}})
    return due_cards.text

def open_anki():
    os.startfile("C:\\Users\\kesh2\\AppData\\Local\\Programs\\Anki\\anki.exe")
    return

def is_anki_open():
    try:
        res = requests.post("http://localhost:8765", json={"action": "version"}, timeout=2)
        return res.status_code == 200
    except requests.exceptions.RequestException:
        return False

def create_deck():
    """
    Create a new Anki deck
    """
    return

def add_to_deck():
    """
    Add a new card to existing Anki deck
    """
    return