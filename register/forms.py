from django import forms
from .models import *

class RegisterForm(forms.ModelForm):
    GENDER_CHIOSE = (
        ("M",'Male'),
        ("F",'Female')
    )
    first_name  = forms.CharField(label='First Name :', widget=forms.TextInput(attrs={"placeholder": "Your First Name"}))
    last_name   = forms.CharField(label='Last Name :', widget=forms.TextInput(attrs={"placeholder": "Your Last Name"}))
    email       = forms.EmailField(label="Eamil Adress :", max_length=254, widget=forms.TextInput(attrs={"placeholder": "Your Email"}))

    age         = forms.DecimalField(label='Age :', widget=forms.TextInput(attrs={"placeholder": "Age"}))
    class Meta:
        model = UserRegister
        fields = [
            'first_name',
            'last_name',
            'email',
            'age',
        ]

class LoginForm(forms.Form):
    userName = forms.CharField(label="UserName :" , widget=forms.TextInput(attrs={
        'placeholder':"username",
        'class':'form-control',
    }))
    password = forms.CharField(label="Password :" , widget=forms.PasswordInput(attrs={
        'placeholder':"Password",
        'class':'from-control',
    }))
    
    