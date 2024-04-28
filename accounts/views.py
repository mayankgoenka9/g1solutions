# from _typeshed import Self
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from datetime import date

import accounts
from .models import Enquiries

# Create your views here.
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    
    else:    
        return render(request,"login.html")

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        subject = 'WELCOME TO THE G1SOLUTIONS CLUB.'
        message = 'Hey '+ firstname +','+ '\n\nWe would like to personally thank you for signing up to our service.\n\nWe established G-One Solutions in order to provide people with the most effective and affordable software services.\n\nWe would love to hear what you think of our services and if there is anything we can improve. If you have any questions, please reply to this email. We are always happy to help!\n\nWarm Regards,\n\n\nG-One Solutions'
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username Already Taken')
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'This Email Is Already Registered')
            return redirect('signup')
        else:
            user = User.objects.create_user(username=username,email=email,password=password,first_name=firstname,last_name=lastname)
            user.save()
            print('user created')
            send_mail(subject, message, settings.EMAIL_HOST_USER, [email])
            auth.login(request,user)
            return redirect('/')
    else:    
        return render(request,"signup.html")
def profile(request):
    if request.user.is_superuser:
        data = Enquiries.objects.all().order_by('date_enquired').reverse()
    else:
        data = Enquiries.objects.filter(user=request.user).order_by('date_enquired').reverse()
    enquiries = {
                "enquiries": data
        }
    return render(request,"profile.html",enquiries)

def enquiry(request):
    return render(request,"enquiry.html")

def send_enquiry(request):
    if request.method == 'POST':
        user_id = request.user.id
        services_list = request.POST.getlist('services')
        services = ", ".join(services_list)
        status = 'pending'
        date_enquired = date.today()
        print(user_id,services,date_enquired)
        enq_inst = Enquiries.objects.create(services=services,date_enquired=date_enquired,status=status,user_id=user_id)
        enq_inst.save()

        #Email Intimation
        email = enq_inst.user.email
        subject = 'Enquiry Status Update.'
        message = 'Hey '+ enq_inst.user.first_name +','+ '\n\nWe have received your service enquiry of '+ enq_inst.services + '. \nWe will be contacting soon regarding your enquiry.\n\nThanks and Regards,\n\n\nG-One Solutions'
        send_mail(subject, message, settings.EMAIL_HOST_USER, [email])

        return redirect('profile')

def close_enquiry(request):
    if request.method=='GET':
        service_id = request.GET.get('id')
        status_of_requested_service = Enquiries.objects.get(id=service_id)
        status_of_requested_service.status = "quotation sent"
        status_of_requested_service.save()

        #Email Intimation
        email = status_of_requested_service.user.email
        subject = 'Enquiry Status Update.'
        message = 'Hey '+ status_of_requested_service.user.first_name+',' + '\n\nI hope we were able to help you with your service enquiry of '+ status_of_requested_service.services + '.\n\nWe have sent you a mail with your quotation prior to this mail, please check for the same.\nWe will be looking forward to connecting with you further.\n\nWarm Regards,\n\n\nG-One Solutions'
        send_mail(subject, message, settings.EMAIL_HOST_USER, [email])

        return redirect("profile")

def logout(request):
    auth.logout(request)
    return redirect('/')


