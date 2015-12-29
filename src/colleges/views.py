from django.shortcuts import render
from .models import College

# Create your views here.


def home(request):
    """TODO: Docstring for home.
    :returns: TODO

    """
    colleges = College.objects.all()
    return render(request, 'colleges/colleges.html', {'colleges': colleges})

