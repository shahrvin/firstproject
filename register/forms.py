from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
User= get_user_model()
# class RegisterForm(forms.ModelForm):
#     GENDER_CHIOSE = (
#         ("M",'Male'),
#         ("F",'Female')
#     )
#     first_name  = forms.CharField(label='First Name :', widget=forms.TextInput(attrs={"placeholder": "Your First Name"}))
#     last_name   = forms.CharField(label='Last Name :', widget=forms.TextInput(attrs={"placeholder": "Your Last Name"}))
#     email       = forms.EmailField(label="Eamil Adress :", max_length=254, widget=forms.TextInput(attrs={"placeholder": "Your Email"}))

#     age         = forms.DecimalField(label='Age :', widget=forms.TextInput(attrs={"placeholder": "Age"}))
#     class Meta:
#         model = UserRegister
#         fields = [
#             'first_name',
#             'last_name',
#             'email',
#             'age',
#         ]

class LoginForm(forms.Form):
    userName = forms.CharField(label="UserName :" , widget=forms.TextInput(attrs={
        'placeholder':"username",
        'class':'form-control',
    }))
    password = forms.CharField(label="Password :" , widget=forms.PasswordInput(attrs={
        'placeholder':"Password",
        'class':'from-control',
    }))

class RegisterForm(forms.Form):
    userName = forms.CharField(label="UserName :" , widget=forms.TextInput(attrs={
        'placeholder':"username",
        'class':'form-control',
    }))

    password = forms.CharField(label="Password :" , widget=forms.PasswordInput(attrs={
        'placeholder':"Password",
        'class':'from-control',
    }))   

    passwordconf = forms.CharField(label="Confirm Password :" , widget=forms.PasswordInput(attrs={
        'placeholder':"Password",
        'class':'from-control',
    })) 

    email = forms.CharField(label="Email :", widget=forms.EmailInput(attrs={
        'placeholder':"Email",
        'class':"from-control",
    }))
    
    def clean_userName (self):
        userName = self.cleaned_data.get('userName')
        qs = User.objects.filter(username = userName)
        if qs.exists():
            raise ValidationError("username already exists ")
        return userName

    
    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        passwordconf = self.cleaned_data.get("passwordconf")
        if password != passwordconf :
            raise ValidationError("Confirm password")
           
        return data