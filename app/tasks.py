from test_app import settings
from celery import shared_task
from django.core.mail import send_mail


@shared_task(bind=True)
def send_email_task(self):
    subject = "Reservation"
    message = "Réservation"
    to_email = "iamchaibsouhail@gmail.com"
    send_mail(
        subject, message, from_email=settings.EMAIL_HOST_USER, recipient_list=[to_email]
    )
    return "task succesful"
