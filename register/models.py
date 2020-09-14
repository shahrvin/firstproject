from django.db import models
from django.forms.widgets import DateInput

# Create your models here.
class UserRegister (models.Model):
    GENDER_CHIOSE = (
        ("M",'Male'),
        ("F",'Female')
    )
    first_name = models.CharField(max_length=100 , null = False , blank= False)
    last_name  = models.CharField(max_length=100 , null = False , blank= False)
    email      = models.EmailField( max_length=254)
    age        = models.DecimalField(decimal_places =0 ,max_digits=2 , blank=True , null = True)
    gender     = models.CharField(max_length= 1 , choices=GENDER_CHIOSE)