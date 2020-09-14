from django import forms
from .models import UserRegister

class RegisterForm(forms.ModelForm):
    GENDER_CHIOSE = (
        ("M",'Male'),
        ("F",'Female')
    )
    first_name  = forms.CharField(label='First Name :', widget=forms.TextInput(attrs={"placeholder": "Your First Name"}))
    last_name   = forms.CharField(label='Last Name :', widget=forms.TextInput(attrs={"placeholder": "Your Last Name"}))
    email       = forms.EmailField(label="Eamil Adress :", max_length=254, widget=forms.TextInput(attrs={"placeholder": "Your Email"}))
    # gender      = forms.ChoiseField(max_length= 1 , choices=GENDER_CHIOSE)
    age         = forms.DecimalField(label='Age :')
    class Meta:
        model = UserRegister
        fields = [
            'first_name',
            'last_name',
            'email',
            # 'gender',
            'age',
        ]