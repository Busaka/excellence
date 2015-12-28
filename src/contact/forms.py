
from django import forms
# from .models import Contact


# class ContactForm(forms.ModelForm):

#     """Docstring for . """
#     class Meta:
#         model = Contact
#         fields = ['email', 'subject',  'message']



class ContactForm(forms.Form):

    """Docstring for . """
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField()
