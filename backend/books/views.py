from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .gutendex_utils import get_book, clean_gutenberg_text, get_random_excerpt, get_random_book
from django.views.decorators.csrf import csrf_exempt
import json
from users.models import SavedArticle
from django.contrib.auth.models import User
from rest_framework import generics
from users.serializers import UserSerializer
import json
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

def home(request):
    return HttpResponse("Hello, world! This is my first Django app.")

def view_book_api(request):
    book = get_random_book()
    return JsonResponse(book)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save_article(request):
    data = request.data
    user = request.user

    article = SavedArticle.objects.create(
        user=user,
        title=data.get('title', 'Untitled'),
        author=data.get('author', ''),
        text_url=data.get('text_url', ''),
    )
    return Response({'message': 'Article saved!', 'id': article.id}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_saved_articles(request):
    print("User:", request.user)
    print("Auth:", request.auth)
    user = request.user
    articles = SavedArticle.objects.filter(user=user).values(
        'title', 'author', 'text_url'
    )
    return Response(list(articles))