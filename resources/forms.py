from django import forms
from .models import Resource
from hr.models import Department

class ResourceForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ResourceForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control mb-3'
            self.fields['sub_category'].required = False
            self.fields['content'].required = False
            self.fields['video'].required = False

    class Meta:
        model = Resource
        fields = ('__all__')

    sub_category = forms.ModelChoiceField(queryset=Department.objects.all())



