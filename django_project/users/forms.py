from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()   #all this to include email in forms

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  #indicates fields and what order in the form


#added later

class UserUpdateForm(forms.ModelForm):   #to update forms cannot change password here
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):   #to update profile
    class Meta:
        model = Profile
        fields = ['image']
