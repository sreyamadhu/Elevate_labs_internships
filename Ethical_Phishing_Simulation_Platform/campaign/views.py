from django.shortcuts import render, redirect
from .models import TargetUser, EmailEvent
from django.utils.timezone import now
from django.db.models import Count
import matplotlib.pyplot as plt
from django.http import HttpResponse
from io import BytesIO
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import CapturedCredential  
from django.shortcuts import get_object_or_404
from .phish import send_phishing_email 
from django.contrib.auth.models import User



def send_phishing_email(user):
    print(f"[TEST] Would send phishing email to: {user.email}")


def home(request):
    users = TargetUser.objects.all()
    return render(request, "home.html", {'users': users})

   
""" 
def track_click(request, user_id):
    user = TargetUser.objects.get(id=user_id)
    EmailEvent.objects.create(user=user, event_type='click', timestamp=now())
    return redirect('/fake-login/')
"""
def track(request, user_id):
    user = get_object_or_404(TargetUser, id=user_id)
    
    # Create a tracking event
    EmailEvent.objects.create(user=user, event_type='click')

    return redirect('fake_login')


def fake_login(request):
    return render(request, 'fake_login.html')


def capture_input(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        pw = request.POST.get('pass')

        # Save credentials to DB
        CapturedCredential.objects.create(username=user, password=pw)

        print(f"Captured credentials: {user}:{pw}")
        return render(request, "education.html")
    else:
        return render(request, "fake_login.html")

def plot_events(request):
    events = EmailEvent.objects.values('event_type').annotate(count=Count('id'))

    if not events:
        return HttpResponse("No event data to display yet.")

    labels = [e['event_type'] for e in events]
    sizes = [e['count'] for e in events]

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    ax.axis('equal')

    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    return HttpResponse(buf.getvalue(), content_type='image/png')

#def send_test_email(request, user_id):
#    user = get_object_or_404(CustomUser, id=user_id)
#    send_phishing_email(user)
#    return redirect('home')
