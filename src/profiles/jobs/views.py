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
        form.save()
    return render(request, 'jobs/post_job.html', {'form': form})

