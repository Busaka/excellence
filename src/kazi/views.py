from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages

from .forms import JobForm
from .models import Kazi

# Create your views here.


def kazi(request):
    jobs = Kazi.objects.filter(publish='yes').order_by('-published')
    return render(request, 'kazi/home.html', {'jobs': jobs})

def post_kazi(request):
    """TODO: Docstring for home.
    :returns: TODO
    """
    form = JobForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your Job has been posted successfully. NOTE: Your Job will have to be reviewed by the moderator before it is published on this site. This could take upto 24 hours.')
        return HttpResponseRedirect('/kazi')
    return render(request, 'kazi/post_job.html', {'form': form})

def kazi_details(request, job_id):
    job_details = Kazi.objects.filter(pk=job_id)
    return render(request, 'kazi/job_details.html', {'job_details': job_details})

def available_jobs(request, job_id):
    job_details = Kazi.objects.filter(pk=job_id)
    return render(request, 'kazi/available_jobs.html', {'job_details': job_details})
