from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookmarkViewSet, FolderViewSet

router = DefaultRouter()
router.register(r'folders', FolderViewSet, basename='folder')
router.register(r'items', BookmarkViewSet, basename='bookmark')

urlpatterns = [
    path('', include(router.urls)),
]
