import requests, random

BASE_URL = "https://gutendex.com/books/"

def get_random_book():
    # Get a random page of English books that have plain text
    num = random.randint(1, 1000)  
    url = f"{BASE_URL}{num}"
    response = requests.get(url).json()
    print(response)

    title = response['title']
    authors = response['authors']
    summary = response['summaries']
    subjects = response['subjects']
    bookshelves = response['bookshelves']
    language = response['languages']
    text_url = response['formats']['text/plain; charset=us-ascii']

    return {"title": title, "authors": authors, "summary": summary, "subjects": subjects, "bookshelves": bookshelves, "language": language, "text_url": text_url}

def get_book(text_url):
    response = requests.get(text_url)
    if response.status_code == 200:
        return response.text
    return None

def clean_gutenberg_text(text):
    start_marker = "*** START OF THE PROJECT GUTENBERG EBOOK"
    end_marker = "*** END OF THE PROJECT GUTENBERG EBOOK"

    # Find the start
    start_idx = text.find(start_marker)
    if start_idx != -1:
        # Move to the end of the line
        start_idx = text.find("\n", start_idx) + 1
        text = text[start_idx:]

    # Find the end
    end_idx = text.find(end_marker)
    if end_idx != -1:
        text = text[:end_idx]

    return text.strip()  # remove leading/trailing whitespace

def get_random_excerpt(text, length=500):
    words = text.split()
    if len(words) < length:
        return "Book too short."

    start = random.randint(0, len(words) - length)
    excerpt = " ".join(words[start:start+length])
    return excerpt