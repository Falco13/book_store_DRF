from django.contrib import admin
from book_store_app.models import Book, Category


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'created_at', 'updated_at', 'is_active', 'category']


admin.site.register(Category)
