from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control signup-input'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control signup-input'}))
    phone_number = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'signup-input'}))

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
            'username':forms.TextInput(attrs={'id':'form-input1', "class":'signup-input'}),
            'first_name':forms.TextInput(attrs={'id':'id_fname', "class":'signup-input'}),
            'last_name':forms.TextInput(attrs={'id':'id_lname', "class":'signup-input'}),
            'email':forms.TextInput(attrs={'id':'id_email', "class":'signup-input'}),
            'phone_number':forms.TextInput(attrs={'id':'id_phone', "class":'signup-input'}),
        }

