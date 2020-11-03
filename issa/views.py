from django.contrib.auth.decorators import login_required 
from rest_framework import status
from django.shortcuts import render, redirect, render_to_response, HttpResponseRedirect
from django.http import HttpResponse, Http404
from django.contrib.auth.forms import UserCreationForm
from .models import User, Business, Activity, NeighbourHood
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
from .forms import SignUpForm, ActivityForm, UserForm, BusinessForm


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
   
    
    
    
        return render(request,'dashboard.html', {"activities":activities, "user":user})
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
        User = User.objects.get(user=current_user)
    except ObjectDoesNotExist:
        return redirect('new-user')

    return render(request,'profiles/user_profile.html',{ 'profile':profile,'activities':activities,'current_user':current_user})

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
    try:
        User = User.objects.filter(user=request.user)
        arr=[]
        for biz in User:
            arr.append(biz.neighbourhood.id)
        if len(arr)>0:
            id=arr[0]
            bussinesses=Bussinesses.objects.filter(business_neighbourhood=id)
        else:
            businesses=Businesses.objects.filter(business_neighbourhood=10000000000)
    except Exception as error:
        raise Http404()
        
        title = "Businesses"

    return render(request,'bussiness/businesses.html', {"id":id, "businesses":businesses})

# function for user edit
@login_required(login_url='/accounts/login/')
def edit_user(request):
    current_user = request.user
    if request.method == 'POST':
        user = User.objects.get(user=request.user)
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
        return redirect('new_profile')
    else:
        form = UserForm()
    return render(request,'profile_edit.html',{'form':form})

# new user function
@login_required(login_url='/accounts/login/')
def new_user(request):
    current_user = request.user
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.user = current_user
            user.userId = request.user.id
            user.save()
        return redirect('new_profile')
    else:
        form = UserForm()
    return render(request, 'profiles/new_profile.html', {"form": form})
# function to handle new businesses
@login_required(login_url='/accounts/login/')
def businesses(request):
    current_user = request.user

    if request.method == 'POST':
        form = BussinessForm(request.POST, request.FILES)
        if form.is_valid():
            bussiness = form.save(commit=False)
            bussiness.user = current_user
            bussiness.save()
        return redirect('biz')

    else:
        form = BussinessForm()
    return render(request, 'business/new_business.html', {"form": form})

