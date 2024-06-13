from django.core.mail import send_mail
from django.conf import settings
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import Enquiry

default_email = settings.DEFAULT_FROM_EMAIL


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def send_enquiry_email(request):
    data = request.data

    try:
        subject = data["subject"]
        name = data["name"]
        email = data["email"]
        message = data["message"]
        from_email = data["email"]
        recipients = [default_email]

        send_mail(subject, message, from_email, recipients, fail_silently=True)
        enquiry = Enquiry(name=name, email=email, subject=subject, message=message)
        enquiry.save()

        return Response({"success": "Your enquiry was sent successfully!"})

    except:
        return Response(
            {"fail": "Enquiry was not sent. Please try again"},
            status=status.HTTP_200_OK,
        )
