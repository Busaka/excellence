from django.shortcuts import render
from .models import HighSchool

# Create your views here.


def home(request):
    """TODO: Docstring for home.
    :returns: TODO

    """
    schools = HighSchool.objects.all()
    # for school in schools:
    # print(schools)

    return render(request, 'high_schools/home.html', {'schools': schools})

def high_school_details(request, uni_id):
    """TODO: Docstring for home.
    :returns: TODO

    """
    high_school_details  = HighSchool.objects.get(pk=uni_id)

    return render(request, 'high_schools/high_school_details.html', {'high_school_details': high_school_details})


