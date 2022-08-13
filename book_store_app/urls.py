from rest_framework import routers
from book_store_app.views import BooksViewSet

router = routers.SimpleRouter()
router.register('books', BooksViewSet)

urlpatterns = []

urlpatterns += router.urls
