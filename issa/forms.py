from pyuploadcare.dj.forms import ImageField
from django import forms
from django.forms import ModelForm
from .models import Profile, NeighbourHood, Business, Activity
from django.contrib.auth.forms import UserCreationForm
from django.contrib .auth.models import User



class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        exclude = ['profile','pub_date']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user']


