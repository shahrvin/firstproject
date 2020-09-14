from django.shortcuts import render
from .forms import RegisterForm
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