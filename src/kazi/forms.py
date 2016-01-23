from django import forms
from .models import Kazi


class JobForm(forms.ModelForm):

    """Docstring for . """
    class Meta:
        model = Kazi
        fields = [
            'school',
            'email',
            'job_title',
            'job_description1',
            ]
