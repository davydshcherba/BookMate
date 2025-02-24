from django.shortcuts import render
from .models import Book

def home(request):
    books = Book.objects.filter(user=request.user) if request.user.is_authenticated else []
    return render(request, "main/index.html", {"books": books})

def profile(request):
    return render(request, 'main/profile.html')