from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import F 
from .models import Book, Bookmark

def home(request):
    if request.user.is_authenticated:
        Book.objects.filter(user=request.user, page_now__gte=F("pages")).delete()       
        books = Book.objects.filter(user=request.user)
    else:
        books = []
    return render(request, "main/index.html", {"books": books})

def profile(request):
    return render(request, "main/profile.html")

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id, user=request.user)
    return render(request, "main/book_detail.html", {"book": book})

def add_bookmark(request):
    if request.method == "POST":
        book_id = request.POST.get("book")
        title = request.POST.get("title")
        content = request.POST.get("bookmark")

        book = get_object_or_404(Book, id=book_id, user=request.user)
        Bookmark.objects.create(book=book, title=title, bookmark=content)

        return redirect("book_detail", book_id=book.id) 

    books = Book.objects.filter(user=request.user)
    return render(request, "main/add_bookmark.html", {"books": books})

def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        pages = request.POST.get("pages")
        page_now = request.POST.get("page_now")

        if request.user.is_authenticated:
            Book.objects.create(user=request.user, title=title, pages=pages, page_now=page_now)
            return redirect("home")  

    return render(request, "main/add_book.html")
