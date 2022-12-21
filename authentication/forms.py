from django import forms
from hr.models import Role


class RegisterForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control mb-3'

    username        = forms.CharField(max_length=50)
    email           = forms.EmailField()
    password        = forms.CharField(widget=forms.PasswordInput)
    confirmation    = forms.CharField(widget=forms.PasswordInput)
    role            = forms.CharField(widget=forms.Select(choices=Role.ROLES))