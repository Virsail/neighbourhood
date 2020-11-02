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
import datetime as dt
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from django.template.loader import render_to_string
#from .token_generator import account_activation_token
from django.http import JsonResponse
from .forms import SignUpForm, ActivityForm, ProfileForm, BusinessForm 


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
# function for the profile page
def user(request):
    current_user = request.user
    activities = Activities.objects.filter(profile = current_user)

    try:
        profile = Profile.objects.get(user=current_user)
    except ObjectDoesNotExist:
        return redirect('new-user')

    return render(request,'profiles/user_profile.html',{ 'profile':profile,'activities':activities,'current_user':current_user})

# fnction that will handle activities posted by user
@login_required(login_url='/accounts/login/')
def activities(request):
    current_user = request.user
    if request.method == 'POST':
        form = activityForm(request.POST, request.FILES)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.profile = current_user
            activity.submitter_id = current_user.id
            activity.save()
        return redirect('dashboard')

    else:
        form = ActivityForm()
    return render(request, 'fatheroffour/new_activity.html', {"form": form})
@login_required(login_url='/accounts/login/')
def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.userId = request.user.id
            profile.save()
        return redirect('NewProfile')
    else:
        form = NewProfileForm()
    return render(request, 'new_profile.html', {"form": form})

