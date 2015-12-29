from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import JobForm

# Create your views here.


def jobs(request):
    """TODO: Docstring for home.
    :returns: TODO
    """
    form = JobForm(request.POST or None)
    if form.is_valid():
        print('THIS IS THE FORM SUBJECT', form.cleaned_data.get('school', ''))
        print('THIS IS THE FORM SUBJECT', form.cleaned_data.get('subject', ''))
        print('THIS IS THE FORM SUBJECT', form.cleaned_data.get('email', ''))
        print('THIS IS THE FORM SUBJECT', form.cleaned_data.get('description', ''))
        form.save()
    return render(request, 'jobs/jobs.html', {'form': form})

