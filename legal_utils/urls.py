from django.urls import path
from .views import CitationGeneratorView, PDFGeneratorView, RelatedLawsView, AmendmentTrackingView

urlpatterns = [
    path('citation/', CitationGeneratorView.as_view(), name='citation-generator'),
    path('pdf/', PDFGeneratorView.as_view(), name='pdf-generator'),
    path('related/', RelatedLawsView.as_view(), name='related-laws'),
    path('amendments/', AmendmentTrackingView.as_view(), name='amendments'),
]
