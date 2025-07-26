from django.core.mail import send_mail
from django.conf import settings

def send_phishing_email(user):
    subject = "Security Alert - Unusual Login Attempt"
    message = f"""
    Dear {user.email},

    We've detected an unusual login attempt on your account.
    Please verify your login activity here:
    http://127.0.0.1:8000/track/{user.id}/

    Regards,
    Security Team
    """
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [user.email],
        fail_silently=False,
    )
