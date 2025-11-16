from celery import shared_task
from django.core.mail import send_mail

from ShopProject import settings


@shared_task
def send_welcome_email(subject , message , recipient):
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[recipient],
        fail_silently=False

    )
    return "Email Sent"
