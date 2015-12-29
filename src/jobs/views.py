from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import JobForm
from .models import Job

# Create your views here.


def jobs(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/home.html', {'jobs': jobs})

def post_job(request):
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

