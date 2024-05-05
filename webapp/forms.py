from django.contrib.auth.forms import UserCreationForm    #26 in diary
from django.contrib.auth.models import User                #27 in diary 
from django import forms                                   #28 in diary
from django.contrib.auth.forms import AuthenticationForm   #29 in diary
from django.forms.widgets import PasswordInput, TextInput   #30 in diary
from .models import Record  #step62 

# Registe/create a user 

class CreateUserForm(UserCreationForm):          #31 steps we use to crete signup form  
    class Meta:

        model = User
        fields= ['username' , 'password1' , 'password2']






# Login a user 
class LoginForm(AuthenticationForm):                 #32 steps we take to craete login authentication
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=input())


#create REcord Form
class CreateRecordForm (forms.ModelForm):
    class Meta:
        #step 63
        model = Record
        fields= ['first_name' , 'last_name' , 'email' , 'phone', 'address' ,'city' ,'province' ,'country']


#update record form
class UpdateRecordForm (forms.ModelForm):
    class Meta:
        #step 64 
        model = Record
        fields= ['first_name' , 'last_name' , 'email' , 'phone', 'address' ,'city' ,'province' ,'country']

