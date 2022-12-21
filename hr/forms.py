import datetime

from django import forms
from .models import Employee, Department
from authentication.models import Login

class ProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control mb-1'

    class Meta:
        model = Employee
        exclude = ('is_new',)


    manager     = forms.ModelChoiceField(queryset=Login.objects.filter(username__in=list(Employee.objects.filter(role=3))))
    sign_date   = forms.DateField(widget=forms.SelectDateWidget)
    start_date  = forms.DateField(widget=forms.SelectDateWidget)



