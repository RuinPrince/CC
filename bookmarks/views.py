from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Bookmark, Folder
from .serializers import BookmarkSerializer, FolderSerializer

class FolderViewSet(viewsets.ModelViewSet):
    serializer_class = FolderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Folder.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BookmarkViewSet(viewsets.ModelViewSet):
    serializer_class = BookmarkSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Bookmark.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

