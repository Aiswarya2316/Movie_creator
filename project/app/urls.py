from django.urls import path
from .views import MovieListCreateAPIView, MovieRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('movies/', MovieListCreateAPIView.as_view(), name='movie-list-create'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyAPIView.as_view(), name='movie-detail'),
]

from rest_framework.routers import DefaultRouter
from .views import MovieViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet)

urlpatterns = router.urls
