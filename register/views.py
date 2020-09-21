from django.shortcuts import render
from .forms import RegisterForm , LoginForm
from django.contrib.auth import login , authenticate
# Create your views here.
def user_create_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, "user_create.html", context)
 
def login_view(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        print(form.cleaned_data)
        userName = form.cleaned_data.get('userName')
        password = form.cleaned_data.get('password')
        user = authenticate(request , username=userName , password = password)
        if user is  not None :
            login(request ,user )
            context['form'] = LoginForm()
        else :
            print("error")

    return render(request, "login.html", context)