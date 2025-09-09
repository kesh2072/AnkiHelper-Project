from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .gutendex_utils import get_book, clean_gutenberg_text, get_random_excerpt, get_random_book

def home(request):
    return HttpResponse("Hello, world! This is my first Django app.")

def view_book_api(request):
    book = get_random_book()
    #book = clean_gutenberg_text(book)
    #excerpt = get_random_excerpt(book, length=80)
    return JsonResponse(book)
