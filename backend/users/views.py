from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import SavedArticle
from rest_framework import generics
from .serializers import UserSerializer
import json
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

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
        excerpt=data.get('excerpt', '')
    )
    return Response({'message': 'Article saved!', 'id': article.id}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_saved_articles(request):
    print("User:", request.user)
    print("Auth:", request.auth)
    user = request.user
    articles = SavedArticle.objects.filter(user=user).values(
        'title', 'author', 'text_url', 'excerpt', 'date_saved'
    )
    return Response(list(articles))

