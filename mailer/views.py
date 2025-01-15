from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from .models import EmailRecord
from django.core.mail import EmailMessage
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

# mailer/views.py
from django.shortcuts import redirect
from django.http import HttpResponse

def signup_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('signup')  # Redirect to the signup page if not authenticated
        return view_func(request, *args, **kwargs)
    return _wrapped_view



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def home(request):
    return HttpResponse("Welcome to the Home Page!")

@login_required
def send_email(request):
    if request.method == "POST":
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        recipient = request.POST.get("recipient")
        cc = request.POST.get("cc")
        bcc = request.POST.get("bcc")

        try:
            # Create the email message object
            email = EmailMessage(
                subject=subject,
                body=message,
                from_email='your_email@gmail.com',
                to=[recipient],
                cc=cc.split(',') if cc else None,
                bcc=bcc.split(',') if bcc else None,
            )

            # Send the email
            email.send()

            # Save the record in the database
            EmailRecord.objects.create(
                subject=subject,
                message=message,
                recipient=recipient,
                cc=cc,
                bcc=bcc,
            )

            return HttpResponse("Email sent successfully!")
        except Exception as e:
            return HttpResponse(f"Error sending email: {e}")

    return render(request, 'mailer/send_email.html')
