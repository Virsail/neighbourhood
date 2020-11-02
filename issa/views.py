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
#from .forms import PostForm, BussinessForm, ProfileForm
import datetime as dt
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from django.template.loader import render_to_string
#from .token_generator import account_activation_token
from django.http import JsonResponse
from .forms import SignUpForm


# Create your views here.
def signPage(request):
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
        return render(request, 'registration/registration_form.html', {'form': form})

# Function for the home page
def dashboard(request):
    
    
    return render(request,'dashboard.html')
# search function
@login_required(login_url='/accounts/login/')
def search_results(request):
    
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_businesses = Business.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'fatheroffour/search.html',{"message":message,"projects": searched_projects})

    else:
     message = "There are currently no businesses"
     return render(request, 'fatheroffour/search.html',{"message":message})

