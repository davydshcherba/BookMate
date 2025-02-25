from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Bookmark

def home(request):
    books = Book.objects.filter(user=request.user) if request.user.is_authenticated else []
    return render(request, "main/index.html", {"books": books})

def profile(request):
    return render(request, 'main/profile.html')

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id, user=request.user)
    return render(request, 'main/book_detail.html', {"book": book})

def add_bookmark(request):
    if request.method == "POST":
        book_id = request.POST.get("book")
        title = request.POST.get("title")
        content = request.POST.get("bookmark")

        book = get_object_or_404(Book, id=book_id, user=request.user)
        Bookmark.objects.create(book=book, title=title, bookmark=content)

        return redirect("book_detail", book_id=book.id)  # Повернення до книги після додавання

    books = Book.objects.filter(user=request.user)
    return render(request, "main/add_bookmark.html", {"books": books})
