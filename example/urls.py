from django.urls import path, include
from .views import HelloAPI, BookAPIMixins, BooksAPIMixins
 
urlpatterns = [
    path("hello/", HelloAPI),
    path("mixin/books/", BooksAPIMixins.as_view()),
    path("mixin/book/<int:bid>/", BookAPIMixins.as_view()),

]