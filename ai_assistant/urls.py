from django.urls import path
from .views import AIChatView, SemanticSearchView, OCRUploadView

urlpatterns = [
    path('chat/', AIChatView.as_view(), name='ai-chat'),
    path('search/', SemanticSearchView.as_view(), name='semantic-search'),
    path('ocr/', OCRUploadView.as_view(), name='ocr-upload'),
]
