from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail,EmailMessage
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    return HttpResponse("Welcome to the Blog Home Page!");
# def send_email(request):
#     subject = 'Hello from sahan hero'
#     message = 'This is a test email sent from a Django application by sahan.'
#     from_email = 'sahanshrestha2000@gmail.com'
#     recipient_list = ['sahanshrestha2k@gmail.com']
#     send_mail(subject, message, from_email, recipient_list)
#     return HttpResponse("Email sent successfully!")
def send_email(request):
    subject = 'Hello from sahan hero'
    message=render_to_string('email_template.html', {'name': 'Sahan'
                                                     ,'course': 'Django'}
   )
    email=EmailMessage(subject, message, 'sahanshrestha2000@gmail.com', ['sahanshrestha2k@gmail.com'])
    email.content_subtype='html'
    email.send()
    return HttpResponse("Email sent successfully!")