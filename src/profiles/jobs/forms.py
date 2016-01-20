from django import forms
from .models import Job


class JobForm(forms.ModelForm):

    """Docstring for . """
    class Meta:
        model = Job
        fields = ['school', 'email',  'job_title',  'job_description']
