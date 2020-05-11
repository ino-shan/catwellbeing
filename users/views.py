from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from .forms import UserRegisterForm
from django.http import QueryDict
from django.views.decorators.csrf import csrf_exempt
from .models import Profile
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from datetime import date
from django.template.loader import get_template
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            subject = 'Welcome to the Cat Wellbeing App community!'
            email_from = settings.EMAIL_HOST_USER
            email_toA = form.cleaned_data.get('email')
            email_to = [email_from, email_toA]
            smessage = 'hi there'
            message=EmailMultiAlternatives(subject=subject,body=smessage,from_email=email_from,to=email_to)
            html_template = get_template("users/signupemail.html").render()
            message.attach_alternative(html_template, "text/html")
            message.send()
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
@csrf_exempt
def profile(request):
    if request.method == 'PUT':
        put = QueryDict(request.body)
        username = put.get('username')
        email = put.get('email')
        password_1 = put.get('password_1')
        password_2 = put.get('password_2')
        address = put.get('address')

        if(request.user!=email and len(User.objects.filter(username=username))==0):
            User.objects.filter(pk=int(request.user.pk)).update(username=username)
            
        Profile.objects.filter(user=request.user).update(address=address)
        the_user = User.objects.get(pk=int(request.user.pk))
        if(put.get('password_1') and put.get('password_2')):
            password_1 = put.get('password_1')
            password_2 = put.get('password_2')
            if(password_1==password_2):
                the_user.set_password(put.get('password_1'))
                the_user.save()

        #need to check if username already exists if so, reject
        # need to check if email already exists if so, reject



    if request.method == "PUT" and  QueryDict(request.body).get('objective')=="VET_APPLICATION":
        PUT =  QueryDict(request.body)
        username = str(put.get('username'))
        email = str(put.get('email'))
        
   
        subject = 'Vet verification appilcation'
        message = str('This is a request from user: ' + username + ' with email: ' + email + ' to get verified.')
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['catwellbeingvet@gmail.com',]
        send_mail( subject, message, email_from, recipient_list )
        
        

    user_profile = Profile.objects.get(user=request.user)
    return render(request, 'users/profile.html', {"user_profile":user_profile})

def logout_view(request):
    logout(request)
    messages.info(request, "You have logged out!")

    return redirect('login')


def signupemail(request):
    subject = 'Welcome to the Cat Wellbeing App community!'
    message = 'Thank you for signing up to CatWellbeing, did you know that as an owner of a cat you should probably know about The Animal Welfare Act 2006 that describes the responsibilty of owners towards their pets, here is a summary : 1.Need for a suitable environment  2.Need for a suitable diet  3.Need to exhibit normal behaviour patterns  4.Need to be housed with,or apart, from other animals   5.Need to be protected from pain,suffering,injury and disease.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['receiver@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return redirect('login')


