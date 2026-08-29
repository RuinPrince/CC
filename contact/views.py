from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.core.mail import send_mail
from django.conf import settings
from .serializers import ContactMessageSerializer

class ContactSubmitView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            contact = serializer.save()

            # Attempt to send email notification (won't crash if email backend is console)
            try:
                send_mail(
                    subject=f"[Civic Companion] New Contact from {contact.name}",
                    message=f"Name: {contact.name}\nEmail: {contact.email}\n\nMessage:\n{contact.message}",
                    from_email=getattr(settings, 'DEFAULT_FROM_EMAIL', 'noreply@civiccompanion.com'),
                    recipient_list=['contact@civiccompanion.com'],
                    fail_silently=True,
                )
            except Exception:
                pass

            return Response({
                "success": True,
                "message": "Thank you! Your message has been received. We'll get back to you soon."
            }, status=201)

        return Response({
            "success": False,
            "errors": serializer.errors
        }, status=400)
