from django.db import models

class Book(models.Model):
    title = models.CharField("Name Book", max_length=150)
    pages = models.IntegerField("Pages in Book")
    page_now = models.IntegerField("Page Now")
    bookmarks = models.JSONField("Bookmarks", default=list)  
    
    def __str__(self):
        return self.title

