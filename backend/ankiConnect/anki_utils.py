import requests

def get_decks():
    decks = requests.post('http://localhost:8765', json={'action': 'deckNames'})
    return decks.text

def get_card_info():
    card_info = requests.post('http://localhost:8765', json={'action': 'cardsInfo', 'params': {'cards': [1761334419606]}}) # can't get this working without hardcoding it 
    return card_info.text

def get_due_cards():
    due_cards = requests.post('http:localhost:8765', json={'action': 'findCards', 'params': {'query': 'is:due'}})
    return due_cards.text

def open_anki():
    """
    If Anki isn't opened on PC, request to open it
    """
    return

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