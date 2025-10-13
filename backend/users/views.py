from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import SavedArticle
import json

@csrf_exempt
def save_article(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # Temporary: get a dummy user (until login is set up)
        user = User.objects.first()

        article = SavedArticle.objects.create(
            user=user,
            title=data.get('title', 'Untitled'),
            author=data.get('author', ''),
            text_url=data.get('text_url', ''),
            excerpt=data.get('excerpt', '')
        )
        return JsonResponse({'message': 'Article saved!', 'id': article.id})

    return JsonResponse({'error': 'POST request required'}, status=400)


def list_saved_articles(request):
    user = User.objects.first()  # same placeholder user
    articles = SavedArticle.objects.filter(user=user).values(
        'title', 'author', 'text_url', 'excerpt', 'date_saved'
    )
    return JsonResponse(list(articles), safe=False)
