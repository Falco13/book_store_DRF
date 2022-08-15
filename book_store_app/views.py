from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from book_store_app.models import Book
from book_store_app.serializers import BookSerializer


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.filter(is_active=True)
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['price', 'created_at', 'category__category_title']
    search_fields = ['title', 'description', 'price', 'category__category_title']
    ordering_fields = ['price', 'created_at']
