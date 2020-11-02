from django.contrib.auth.decorators import login_required 
from rest_framework import status
from django.shortcuts import render, redirect, render_to_response, HttpResponseRedirect
from django.http import HttpResponse, Http404
from django.contrib.auth.forms import UserCreationForm
#from .models import Profile, Businesses, Posts
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.views import APIView
from .forms import PostForm, BussinessForm, ProfileForm
import datetime as dt
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from .token_generator import account_activation_token
from django.http import JsonResponse
from .forms import SignUpForm


# Create your views here.
def registerPage(request):
     if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('dashboard.html')
     else:
        form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})
def page(request):
   return render(request, 'dashboard.html')
# Function for the home page
def dashboard(request):
    try:
        profile = Profile.objects.filter(user_id=request.user.id)
        arr = []
        for new in profile:
            arr.append(new.neighbourhood.id)
        if len(arr)>0:
            id = arr[0]
            posts=Posts.objects.filter(neighbourhood=id)
        else:
            posts=Posts.objects.filter(neighbourhood=10000000000)
    except Exception as e:
        raise Http404()
    
    return render(request,'home.html', {"posts":posts, "profile":profile})


