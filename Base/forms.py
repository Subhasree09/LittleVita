from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    phone_number = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number']   
        labels = {
            'username':'Username',
            'first_name':'First Name',
            'last_name':'Last Name',
            'email':'Email',
            'phone_number':'Phone Number',
        }     

        widgets ={
            'username':forms.TextInput(attrs={'id':'form-input1'}),
            'first_name':forms.TextInput(attrs={'id':'id_fname'}),
            'last_name':forms.TextInput(attrs={'id':'id_lname'}),
            'email':forms.TextInput(attrs={'id':'id_email'}),
            'phone':forms.TextInput(attrs={'id':'id_phone'}),
        }

