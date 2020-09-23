from django.shortcuts import render
from .forms import RegisterForm , LoginForm
from django.contrib.auth import login , authenticate , get_user_model
# # Create your views here.
# def user_create_view(request):
#     form = RegisterForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = RegisterForm()
#     context = {
#         'form': form
#     }
#     if request.user.is_authenticated :
#         context['new'] = 'is authenticated'
#     return render(request, "user_create.html", context)
 
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

User = get_user_model()
def register_view(request):
    error_css_class = "text-danger"
    required_css_class = "required"
    form = RegisterForm(request.POST or None)
    context = {
        'form':form
    }
    if form.is_valid():
        print(form)
        userName = form.cleaned_data.get('userName')
        password = form.cleaned_data.get('password')
        email    = form.cleaned_data.get('email')
        new_user = User.objects.create_user(username =userName , email = email, password = password )

    return render(request, "register.html", context)