from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForms
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'registration/home.html', {'section':'home'})
""" 
def user_login(request):
    if request.method == 'POST':
        form= LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user= authenticate(request, username=cd['username'],password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated''successfully')
                else:
                    return HttpResponse('Disable Account')
            else: 
                return HttpResponse ("Invalid login")
    else:
        form=LoginForm()
    return render(request, 'account/login.html',{'form':form}) """
# Create your views here.

