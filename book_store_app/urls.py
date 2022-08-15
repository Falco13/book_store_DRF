from django.urls import path
from rest_framework import routers
from book_store_app.views import BooksViewSet, RegisterView, ProfileUserView

router = routers.SimpleRouter()
router.register('books', BooksViewSet)

urlpatterns = [
    path('signup/', RegisterView.as_view()),
    path('profile/', ProfileUserView.as_view()),
]

urlpatterns += router.urls
