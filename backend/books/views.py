from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .gutendex_utils import get_book, clean_gutenberg_text, get_random_excerpt, get_random_book
from django.views.decorators.csrf import csrf_exempt
import json
from users.models import SavedArticle
from django.contrib.auth.models import User

def home(request):
    return HttpResponse("Hello, world! This is my first Django app.")

def view_book_api(request):
    book = get_random_book()
    #book = clean_gutenberg_text(book)
    #excerpt = get_random_excerpt(book, length=80)
    return JsonResponse(book)

@csrf_exempt
def save_article(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user = User.objects.first()  # placeholder user for now
        SavedArticle.objects.create(
            user=user,
            title=data.get("title"),
            author=data.get("author"),
            subject=data.get("subject"),
            bookshelves=data.get("bookshelves"),
            language=data.get("language"),
            text_url = data.get("text_url", "")
        )
        return JsonResponse({"message": "Book saved!"})
    return JsonResponse({"message": "Invalid request"}, status=400)

@csrf_exempt
def list_saved_articles(request):
    # For now, get the first user as a placeholder
    user = User.objects.first()
    saved_articles = SavedArticle.objects.filter(user=user)

    data = []
    for article in saved_articles:
        data.append({
            "title": article.title,
            "author": article.author,
            "subject": article.subject,
            "bookshelves": article.bookshelves,
            "language": article.language,
            "text_url": article.text_url,
        })

    return JsonResponse(data, safe=False)