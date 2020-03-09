from django.shortcuts import render, redirect
from . import forms

# Create your views here.

def signup(request):
    if request.method == 'POST':
        user_form = forms.UserCreateForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()

            return redirect('accounts:login')

    else:
        user_form = forms.UserCreateForm()

    context = {'user': user_form}

    return render(request, 'accounts/signup.html', context)
