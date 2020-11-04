from django.contrib.auth.decorators import login_required 
from rest_framework import status
from django.shortcuts import render, redirect, render_to_response, HttpResponseRedirect
from django.http import HttpResponse, Http404
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Business, Activity, NeighbourHood
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
import datetime as dt
#from .views import RegisterAPI
from rest_framework import generics, permissions
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from .forms import SignUpForm, ActivityForm, ProfileForm, BusinessForm
from django.http import JsonResponse




# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


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
    
    return render(request,'dashboard.html', {"activity":activities})



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
def user_profile(request):
    current_user = request.user
    activity = Activity.objects.filter(user = current_user)

    try:
        profile = Profile.objects.get(user=current_user)
    except ObjectDoesNotExist:
        return redirect('new-user')

    return render(request,'profiles/user_profile.html',{ 'profile':profile,'activity':activity,'current_user':current_user})

# fnction that will handle activities posted by user
@login_required(login_url='/accounts/login/')
def activities(request):
    current_user = request.user
    if request.method == 'POST':
        form = ActivityForm(request.POST, request.FILES)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.profile = current_user
            activity.submitter_id = current_user.id
            activity.save()
        return redirect('dashboard')

    else:
        form = ActivityForm()
    return render(request, 'fatheroffour/new_activity.html', {"form": form})

# 

def display_business(request):
    current_user = request.user
    
       
    

    return render(request,'bussiness/businesses.html', {"id":id, "businesses":businesses})


# function for user edit
@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
        return redirect('new_profile')
    else:
        form = ProfileForm()
    return render(request,'profiles/profile_edit.html',{'form':form})

# new user function
@login_required(login_url='/accounts/login/')
def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.userId = request.user.id
            profile.save()
        return redirect('new_profile')
    else:
        form = ProfileForm()
    return render(request, 'profiles/new_profile.html', {"form": form})


# function to handle new businesses
@login_required(login_url='/accounts/login/')
def businesses(request):
    current_user = request.user

    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            bussiness = form.save(commit=False)
            bussiness.user = current_user
            bussiness.save()
        return redirect('biz')

    else:
        form = BusinessForm()
    return render(request, 'bussiness/new_business.html', {"form": form})



