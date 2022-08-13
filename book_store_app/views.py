from rest_framework import generics, viewsets
from book_store_app.models import Book
from book_store_app.serializers import BookSerializer


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.filter(is_active=True)
    serializer_class = BookSerializer
