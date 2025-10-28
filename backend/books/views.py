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
from users.serializers import SavedArticleSerializer
import deepl
import os
from dotenv import load_dotenv

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
    print(data)
    print(data.get('text_url', 'could not retrieve text url'))

    article = SavedArticle.objects.create(
        user=user,
        title=data.get('title', 'Untitled'),
        author=data.get('author', ''),
        text_url=data.get('text_url', ''),
    )
    return Response({'message': 'Article saved!', 'id': article.id}, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_article(request, article_id):
    user = request.user
    try:
        article = SavedArticle.objects.get(id=article_id, user=user)
        article.delete()
        return Response({'message': 'Article deleted'}, status=status.HTTP_200_OK)
    except SavedArticle.DoesNotExist:
        return Response({'message': 'Issue deleting article'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_saved_articles(request):
    user = request.user
    books = SavedArticle.objects.filter(user=user)
    serializer = SavedArticleSerializer(books, many=True)
    return Response(serializer.data)

load_dotenv()
auth_key = os.getenv("DEEPL_API_KEY")

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def deepl_translate(request):
    text = request.data.get("text", "")
    if not text:
        return Response({"error": "no text provided"}, status=400)
    deepl_client = deepl.DeepLClient(auth_key)
    translation = deepl_client.translate_text(text, target_lang="DE")
    return Response({"translation": translation.text})