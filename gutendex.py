import requests, random

BASE_URL = "https://gutendex.com/books"

def get_random_book():
    # Get a random page of English books that have plain text
    random_page = random.randint(1, 500)  
    url = f"{BASE_URL}?languages=en&mime_type=text%2Fplain&page={random_page}"
    response = requests.get(url).json()

    books = response["results"]
    if not books:
        return None

    book = random.choice(books)

    title = book["title"]
    author = book["authors"][0]["name"] if book["authors"] else "Unknown"
    formats = book["formats"]

    # Now it’s much more likely to exist
    text_url = (
        formats.get("text/plain; charset=utf-8")
        or formats.get("text/plain")
    )

    return {"title": title, "author": author, "text_url": text_url}


def download_book_text(text_url):
    response = requests.get(text_url)
    if response.status_code == 200:
        return response.text
    return None


def get_random_excerpt(text, length=500):
    words = text.split()
    if len(words) < length:
        return "Book too short."

    start = random.randint(0, len(words) - length)
    excerpt = " ".join(words[start:start+length])
    return excerpt

def get_book_by_id(book_id):
    url = f"{BASE_URL}{book_id}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

if __name__ == "__main__":
    # book = get_random_book()
    # print(f"📖 {book['title']} — {book['author']}")
    # print(book)

    # if book["text_url"]:
    #     text = download_book_text(book["text_url"])
    #     excerpt = get_random_excerpt(text, length=80)  # ~80 words
    #     print("\n--- Random Excerpt ---\n")
    #     print(excerpt)
    # else:
    #     print("No plain text available for this book.")
    
    # random_page = random.randint(1, 500)  
    # url = f"{BASE_URL}?languages=en&mime_type=text%2Fplain&page={random_page}"
    #BASE_URL = "https://gutendex.com/books/"
    #print(get_book_by_id(6522))
    # response = requests.get(url).json()
    print(download_book_text('https://www.gutenberg.org/ebooks/6522.txt.utf-8'))

    # books = response["results"]
    # print(books)

"""
{'id': 6522, 'title': 'Fruit-Gathering', 'authors': [{'name': 'Tagore, Rabindranath', 'birth_year': 1861, 'death_year': 1941}], 'summaries': ['"Fruit-Gathering" by Rabindranath Tagore is a poetic collection that was originally written in Bengali and later translated into English by the author himself, published in the early 20th century. This work embodies Tagore\'s contemplative exploration of themes such as love, nature, life, and spirituality, reflecting the philosophical traditions prevalent in his time. The poems dive into the depths of human emotion and the connection between the individual and the universe, encapsulating the essence of life\'s transient beauty.  The collection consists of a series of lyrical pieces that weave together personal reflection and universal truths. Tagore speaks of the journey of the soul, using rich imagery to illustrate the cycles of nature and the human experience. He explores the contrasts of joy and sorrow, abundance and lack, spiritual awakening, and the search for deeper meaning amidst life\'s chaos. The poems resonate with a sense of longing and the desire for unity with the divine, ultimately inviting readers to reflect on their own place within the grand tapestry of existence. (This is an automatically generated summary.)'], 'translators': [], 'subjects': ['Bengali poetry -- Translations into English', 'Indic poetry -- Translations into English', 'Tagore, Rabindranath, 1861-1941 -- Translations into English'], 'bookshelves': ['Category: Poetry'], 'languages': ['en'], 'copyright': False, 'media_type': 'Text', 'formats': {'text/html': 'https://www.gutenberg.org/ebooks/6522.html.images', 'application/epub+zip': 'https://www.gutenberg.org/ebooks/6522.epub3.images', 'application/x-mobipocket-ebook': 'https://www.gutenberg.org/ebooks/6522.kf8.images', 'application/rdf+xml': 'https://www.gutenberg.org/ebooks/6522.rdf', 'image/jpeg': 'https://www.gutenberg.org/cache/epub/6522/pg6522.cover.medium.jpg', 'text/plain; charset=us-ascii': 'https://www.gutenberg.org/ebooks/6522.txt.utf-8', 'application/octet-stream': 'https://www.gutenberg.org/files/6522/6522-0.zip'}, 'download_count': 845}
"""