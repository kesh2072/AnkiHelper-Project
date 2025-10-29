import nltk
sent = "GeeksforGeeks is a great learning platform. \
It is one of the best for Computer Science students."
print(nltk.word_tokenize(sent))
print(nltk.sent_tokenize(sent))

def tokenise_words(text):
    """
    Pass in article / book text, and return with tokens (that I can then upload to database - maybe also need article title?)
    This returns a list of all the individual words
    """ 
    tokens = nltk.word_tokenize(text)
    return tokens

def tokenise_sentence(text):
    """
    This tokenises the text into sentences (idk how I'll integrate yet, but will be useful later on so we can extract 
    context for words)
    """
    tokens = nltk.sent_tokenize(text)
    return tokens

from nltk.stem import PorterStemmer

def stemmer(tokens):
    """
    Stemming function to get the stem of words (e.g. 'playing' / 'played' -> 'play')
    Placeholder function for now until I've integrated the rest of the tokenisation stuff
    Also this algorithm was just designed for English, so probably need to find other algorithms for other languages maybe?
    """
    porter = nltk.stem.PorterStemmer()
    stem_words = []
    for word in tokens:
        stem_words.append(porter.stem(word))
    
    return stem_words