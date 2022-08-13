from rest_framework import serializers
from book_store_app.models import Book


class BookSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source='category.category_title')

    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'price', 'created_at', 'updated_at', 'is_active', 'category']
