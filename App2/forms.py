
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Product

class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email']

class SigninForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'



