from rest_framework import generics
from book_store_app.models import Book
from book_store_app.serializers import BookSerializer


class BookAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.filter(is_active=True)
    serializer_class = BookSerializer


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.filter(is_active=True)
    serializer_class = BookSerializer
