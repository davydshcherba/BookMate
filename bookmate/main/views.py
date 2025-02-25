from django.shortcuts import render,get_object_or_404
from .models import Book

def home(request):
    books = Book.objects.filter(user=request.user) if request.user.is_authenticated else []
    return render(request, "main/index.html", {"books": books})

def profile(request):
    return render(request, 'main/profile.html')
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id,user=request.user)
    return render(request, 'main/book_detail.html', {"book": book})