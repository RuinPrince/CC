from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet

router = DefaultRouter()
router.register(r'items', NoteViewSet, basename='note')

urlpatterns = [
    path('', include(router.urls)),
]
