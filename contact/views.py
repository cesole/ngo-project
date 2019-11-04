from django.shortcuts import render
from .form import *
from django.core.mail import EmailMessage, send_mail
from django.conf import settings

# Create your views here.
def Contact(request):
    Contact_Form = ContactForm
    if request.method == 'POST':
        form = Contact_Form(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name')
            contact_email = request.POST.get('contact_email')
            contact_content = request.POST.get('content')

            template = get_template('contact_form.txt')
            context = {
                'contact_name' : contact_name,
                'contact_email' : contact_email,
                'contact_content' : contact_content,
            }
            
            content = template.render(context)

            email = EmailMessage(
                "New contact form email",
                content,
                settings.EMAIL_HOST_USER,
		        ['ceci.abt@gmail.com'],
                headers = { 'Reply To': contact_email }
            )

            email.send()

            return redirect('index')
    return render(request, 'contact.html', {'form':Contact_Form })
    
    
