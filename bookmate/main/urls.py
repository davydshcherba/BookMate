from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('profile', views.profile, name='profile'),
    path('book/<int:book_id>', views.book_detail, name='book_detail'),
]
