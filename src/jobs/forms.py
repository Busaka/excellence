from django import forms
from .models import Job


class JobForm(forms.ModelForm):

    """Docstring for . """
    class Meta:
        model = Job
        fields = ['school', 'email',  'subject',  'description']
