from django.shortcuts import render
from .models import College

# Create your views here.


def home(request):
    """TODO: Docstring for home.
    :returns: TODO

    """
    colleges = College.objects.all()
    return render(request, 'colleges/colleges.html', {'colleges': colleges})

def college_details(request, uni_id):
    """TODO: Docstring for home.
    :returns: TODO

    """
    college_details  = College.objects.get(pk=uni_id)

    return render(request, 'colleges/college_details.html', {'college_details': college_details})


