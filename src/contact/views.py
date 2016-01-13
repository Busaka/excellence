from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponseRedirect
from django.contrib import messages

from .forms import ContactForm

# Create your views here.


def contact(request):
    """TODO: Docstring for home.
    :returns: TODO
    """
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print('THIS IS THE FORM SUBJECT', form.cleaned_data.get('subject', ''))
        print('THIS IS THE FORM SUBJECT', form.cleaned_data.get('email', ''))
        print('THIS IS THE FORM SUBJECT', form.cleaned_data.get('message', ''))

        subject = form.cleaned_data.get('subject', '')
        from_email = form.cleaned_data.get('email', '')
        message = form.cleaned_data.get('message', '')

        send_mail(subject, message, from_email, ['lxbusaka07@gmail.com'], fail_silently=False)
        messages.success(request, 'Email sent successfully!')
        return HttpResponseRedirect('/')
    return render(request, 'contact/contact.html', {'form': form})

