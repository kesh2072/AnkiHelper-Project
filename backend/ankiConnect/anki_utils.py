import requests

def get_decks():
    decks = requests.post('http://localhost:8765', json={'action': 'deckNames'})
    return decks.text

def get_card_info():
    card_ids = []
    card_info = requests.post('http://localhost:8765', json={'action': 'cardsInfo', 'params': {'query': card_ids}})
    return card_info.text

def get_due_cards():
    due_cards = requests.post('http:localhost:8765', json={'action': 'findCards', 'params': {'query': 'is:due'}})
    return due_cards.text


