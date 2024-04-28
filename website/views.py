from django.shortcuts import render,redirect
from django.core.mail import BadHeaderError, send_mail
from django.contrib import messages

def home(request):
    return render(request,'home.html')

def contactus(request):
    if request.method=='POST':
        subject = request.POST['subject']
        message = request.POST['message']
        from_email = request.POST['from_email']
        if subject and message and from_email:
            try:
                send_mail(subject, message, from_email, ['g1solsindia@gmail.com'])
                return redirect('/')
            except BadHeaderError:
                return messages.info(request,'Invalid header found.')
        else:
            # In reality we'd use a form class
            # to get proper validation errors.
            messages.info(request,'Make sure all fields are entered and valid.')
            return redirect('contactus')
    else:
        return render(request,'contactus.html')


