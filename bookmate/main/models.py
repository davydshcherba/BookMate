from django.db import models
from django.contrib.auth.models import User 
class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    title = models.CharField("Name Book", max_length=150)
    pages = models.IntegerField("Pages in Book")
    page_now = models.IntegerField("Page Now")

    def __str__(self):
        return self.title

class Bookmark(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="bookmarks")
    title = models.CharField("Name of Bookmark", max_length=150)
    bookmark = models.TextField("Bookmark Content")

    def __str__(self):
        return f"{self.title} (Page {self.bookmark})"
