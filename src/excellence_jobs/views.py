from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q

from .forms import JobForm
from .models import Job

# Create your views here.


def kazi(request):
    jobs = Job.objects.filter(publish='yes').order_by('-pub_date')
    return render(request, 'excellence_jobs/home.html', {'jobs': jobs})

def post_kazi(request):
    """TODO: Docstring for home.
    :returns: TODO
    """
    form = JobForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your Job has been posted successfully. NOTE: Your Job will have to be reviewed by the moderator before it is published on this site. This could take upto 24 hours.')
        return HttpResponseRedirect('/excellence_jobs')
    return render(request, 'excellence_jobs/post_job.html', {'form': form})

def kazi_details(request, job_id):
    job_details = Job.objects.filter(pk=job_id)
    return render(request, 'excellence_jobs/job_details.html', {'job_details': job_details})

def available_jobs(request, job_title):
    # print(job_title)
    query_terms = job_title.split(" ")
    print(query_terms)
    term1 = query_terms[0]
    try:
        term2 = query_terms[2]
    except:
        term2 = 'empty'

    job_details = Job.objects.filter(publish='yes').filter(Q(job_title__icontains=term1) | Q(job_title__icontains=term2)).order_by('-pub_date')
    
    return render(request, 'excellence_jobs/available_jobs.html', {'job_details': job_details})
