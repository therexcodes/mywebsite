from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from .models import Services
from .models import Project
from .models import ContactInfo
from .models import SubscribedUser
from django.contrib import messages

#below import for email
from django.core.mail import send_mail
from django.conf import settings
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Create your views here.
class Brandname():
    blogbrand = 'Therexblog'
    brandname = 'Therexcodes'


def home(request):
    if request.method == 'POST':
        name= request.POST['name']
        email = request.POST['email']
        subject = request.POST['email_title']
        message = request.POST['message']
        
        #email sending
        send_mail(
            subject,
            f"Message from: {name}, \n {message}",
            email,
            ['therexui@gmail.com'],
            fail_silently=False
            
        )
        
        messages.success(request, "Thanks For Reaching Out! We'll Reply Soon..")
        return redirect('/')
    
    services = Services.objects.all()
    projects = Project.objects.all()
    contact_info = ContactInfo.objects.all()
    
    context = {
        'contact_info': contact_info,
        'services': services,
            'bn': Brandname.brandname,
            'projects': projects
        }
    return render (request, 'home.html',context )


def service(request):
    
    services = Services.objects.all()
    contact_info = ContactInfo.objects.all()
    
    context = {
        'contact_info':contact_info,
        'services': services,
            'bn': Brandname.brandname
        }
    
    return render (request, 'service.html' , context)


def about(request):
    contact_info = ContactInfo.objects.all()
    
    contact_info = ContactInfo.objects.all()
    
    context = {
        'bn': Brandname.brandname,
        'contact_info': contact_info
        }
    return render(request, 'about.html', context)


def projects(request):
    projects = Project.objects.all()
    contact_info = ContactInfo.objects.all()
    
    context =  {
        'contact_info':contact_info,
        'bn': Brandname.brandname,
        'projects': projects
    }
    return render(request, 'projects.html', context)


def contact(request):
    if request.method == 'POST':
        name= request.POST['name']
        email = request.POST['email']
        subject = request.POST['email_title']
        message = request.POST['message']
        
        #email sending
        send_mail(
            subject,
            f"Message from: {name}, \n {message}",
            email,
            ['therexui@gmail.com'],
            fail_silently=False
            
        )
        
        messages.success(request, "Thanks For Reaching Out! We'll Reply Soon..")
        return redirect('/contact')
    
    contact_info = ContactInfo.objects.all()
    
    context = {
        'bn': Brandname.brandname,
        'contact_info': contact_info
        }
    
    return render(request, 'contact.html', context )


def blog(request):
    contact_info = ContactInfo.objects.all()
    context = {
        'contact_info': contact_info,
        'bn':Brandname.blogbrand
        }
    
    return render(request, 'blog.html', context)


def subscribe(request):
    if request.method =="POST":
        sub_email = request.POST.get('Subemail', None)
        
        if not sub_email:
                messages.error(request, "you must type legit email to subscribe")
                return redirect("/")
            
        subscribe_user = SubscribedUser.objects.filter(email=sub_email).first()
        if subscribe_user:
                messages.error(request, "Email already used!")
                return redirect(request.META.get("HTTP_REFERER","/"))
        
        try:
            validate_email(sub_email)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect("/")
        
        
        subscriber_email = SubscribedUser()
        subscriber_email.email = sub_email
        subscriber_email.save()
        messages.success(request, f"email successfully subscribed")
        return redirect(request.META.get("HTTP_REFERER","/"))
    
    return render(request, 'info.html')