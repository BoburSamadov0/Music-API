from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import SongsModelViewSet, AlbumsModelViewSet, ArtistModelViewSet

router = DefaultRouter()
router.register('songs', SongsModelViewSet)
router.register('albums', AlbumsModelViewSet)
router.register('artists', ArtistModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
