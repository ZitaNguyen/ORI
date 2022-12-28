from django import forms
from .models import Employee, Template
from authentication.models import Login

class ProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for field in ['name','manager','role','title','department','template','status']:
            self.fields[field].widget.attrs['class'] = 'form-control mb-3'

    class Meta:
        model = Employee
        exclude = ('is_new', 'task')


    manager     = forms.ModelChoiceField(queryset=Login.objects.filter(username__in=list(Employee.objects.filter(role=3))))
    sign_date   = forms.DateField(widget=forms.SelectDateWidget)
    start_date  = forms.DateField(widget=forms.SelectDateWidget)
    template    = forms.ModelMultipleChoiceField(queryset=Template.objects.all())



