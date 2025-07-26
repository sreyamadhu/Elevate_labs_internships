from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_phishing_email(user):
    subject = "Important: Verify Your Account"
    html_content = render_to_string("phish_template.html", {
        'user': user,
        'tracking_url': f"http://127.0.0.1:8000/track/{user.id}/"
    })
    msg = EmailMultiAlternatives(subject, '', 'your_email@gmail.com', [user.email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
