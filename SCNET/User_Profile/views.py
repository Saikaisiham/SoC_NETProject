from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from itertools import chain
import random
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib.auth import authenticate,login ,logout
from .forms import NewUserForm , PerPage
import logging
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

User = get_user_model()

logger = logging.getLogger(__name__)

# Create your views here.




def register(request):
    page = 'register'
    form = NewUserForm()

    register_url = reverse('User_Profile:register')
    

    if request.method == 'POST' :
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('User_Profile:per_page')
        else : 
            messages.error(request,'An error accured during registration')

    context = {
        'page' : page ,
        'form' : form,
        'register_url': register_url
    }
    return render(request,'userprofile/login_register.html',context)


def loginpage(request):
    page = 'login'

    login_url = reverse('User_Profile:login')


    # if the user already connected
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')


        try : 
            user = User.objects.get(username = username)
            
        except :
            messages.error(request,'User doesnt exist ')

        user = authenticate(request,username = username , password = password)

        if user is not None :
            login(request,user)
            return redirect('/')

        else :
            messages.error(request,'Username or password doesnt exist')

    context = {
        'page' : page ,
        'login_url': login_url
    }
    return render(request,'userprofile/login_register.html',context)



def logoutUser(request):
    login_url = reverse('User_Profile:login')
    # delete the token of the user
    logout(request)
    return render(request,'userprofile/login_register.html',{'login_url': login_url})


def per_page_view(request):
    logger.debug('per_page_view called')
    per_url = reverse('User_Profile:per_page')
    form = PerPage()
    if request.method == 'POST':
        form = PerPage(request.POST, request.FILES)
        if form.is_valid():
            per_page = form.save(commit=False)
            per_page.user = request.user
            per_page.save()
            return redirect('/')
    else:
        form = PerPage()

    context = {
        'form': form,
        'per_url': per_url
    }
    return render(request, 'userprofile/per_page.html', context)





