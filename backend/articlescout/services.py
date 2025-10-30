import tokeniser
from users.models import UserWord, ArticleWord, Article
from ankiConnect.anki_utils import get_due_cards

def tokenise_article():
    """
    placeholder for now until I've set up API stuff to pass in articles
    """
    tokens = tokeniser.tokenise_words()
    return 

def recommend_article():
    """
    This function searches your Anki deck for all of the cards that you have due, and then searches this against the database
    for articles which have these words
    TO-DO:
    - Add in ranking system, so we get articles with the highest quantity of matched words
    """
    due_words = get_due_cards()
    articles = Article.objects.filter(articleword__word_id__in=due_words).distinct()
    return articles

