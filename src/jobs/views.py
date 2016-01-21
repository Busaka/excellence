from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages

from .forms import JobForm
from .models import Job

# Create your views here.


def jobs(request):
    jobs = Job.objects.filter(publish='yes')
    return render(request, 'jobs/home.html', {'jobs': jobs})

def post_job(request):
    """TODO: Docstring for home.
    :returns: TODO
    """
    form = JobForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your Job has been posted successfully. NOTE: Your Job will have to be reviewed by the moderator before it is published on this site. This could take upto 24 hours.')
        return HttpResponseRedirect('/jobs')
    return render(request, 'jobs/post_job.html', {'form': form})

def job_details(request, job_id):
    job_details = Job.objects.filter(pk=job_id)
    return render(request, 'jobs/job_details.html', {'job_details': job_details})
