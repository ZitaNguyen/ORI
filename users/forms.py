from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']
        widgets = {
            'username'  : forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Username'},),
            'email'     : forms.EmailInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Email'}),
            'role'      : forms.Select(attrs={'class': 'form-select mb-3'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'email', 'password1', 'password2', 'role']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].label = ""

        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Password Confirmation'})