# accounts/forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import Member

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Member
        fields = ('username', 'email', 'first_name', 'last_name', 'level', 'status')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Member
        fields = ('username', 'email', 'first_name', 'last_name', 'level', 'status')


class MemberForm(forms.ModelForm):

    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'level', 'status']
    
    
