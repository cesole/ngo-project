from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from .forms import *
from django.template import loader
import os


def Contact(request):
    Contact_Form = ContactForm
    if request.method == 'POST':
        form = Contact_Form(data=request.POST)

        if form.is_valid():
            name = request.POST.get('name')
            subject = request.POST.get('subject')
            email = request.POST.get('email')
            content = request.POST.get('content')
            send_mail(subject, content, 'ceci.abt@gmail.com', [email], fail_silently=False)
            if send_mail:
                messages.success(request, "Your message has been sent")
            else:
                messages.error(request,'Error in form.Try Again')
        else:
            form = EmailForm(request.POST)

    return render(request, 'contact.html', {'form':Contact_Form })
    
    
