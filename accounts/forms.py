from django.contrib.auth import get_user_model, models
from django.contrib.auth.forms import UserCreationForm
from . import models
from django import forms


class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()
        exclude = ('username.help_text',)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].label = ""
            
        
        self.fields['username'].widget.attrs = {
            'placeholder': 'Username',
            'class': "input-style"
        }

        self.fields['email'].widget.attrs = {
            'placeholder': 'Email',
            'class': "input-style"
        }

        self.fields['password1'].widget.attrs = {
            'placeholder': 'Password',
            'class': "input-style"
        }

        self.fields['password2'].widget.attrs = {
            'placeholder': 'Confirm Password',
            'class': "input-style"
        }