from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from . import forms

# Create your views here.

def signin(request):
    form = forms.UserLoginForm()    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard:dashboard')
        else:
            context = {
                'form': form,
                'error': "Username or Password is incorrect"
            }
    else:
        context = {
            'form': form
        }
    return render(request, 'accounts/login.html', context)


def signout(request):
    logout(request)
    return redirect("index")

def signup(request):
    if request.method == 'POST':
        user_form = forms.UserCreateForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()            
            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('password1')

            user_auth = authenticate(username=username, password=password)

            if user_auth is not None:
                login(request, user_auth)
                return redirect('dashboard:dashboard')

    else:
        user_form = forms.UserCreateForm()

    context = {'user': user_form}

    return render(request, 'accounts/signup.html', context)
