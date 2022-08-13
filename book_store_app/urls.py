from django.urls import path
from book_store_app.views import BookAPIView, BookDetailView

urlpatterns = [
    path('books/', BookAPIView.as_view()),
    path('book/<int:pk>', BookDetailView.as_view()),
]
