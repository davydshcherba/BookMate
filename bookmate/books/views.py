import os
from django.conf import settings
from django.shortcuts import render

def search_books(request):
    return render(request, 'books/search_results.html')
