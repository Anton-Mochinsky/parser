from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_reset_email(email, reset_link):
    send_mail(
        'Password Reset',
        f'Click the link to reset your password: {reset_link}',
        'no-reply@o2rus.com',
        [email],
    )
