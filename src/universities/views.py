from django.shortcuts import render
from .models import LocalUniversities, InternationalUniversities


# Create your views here.


def home(request):
    """TODO: Docstring for home.
    :returns: TODO

    """
    # files = University.objects.all()
    # for f in files:
    # print(f)

    return render(request, 'universities/universities.html', {'files': files})

def local_universities(request):
    """TODO: Docstring for home.
    :returns: TODO

    """
    universities  = LocalUniversities.objects.all()
    # for f in files:
    # print(f)

    return render(request, 'universities/local_universities.html', {'universities': universities})

def international_universities(request):
    """TODO: Docstring for home.
    :returns: TODO

    """
    universities = InternationalUniversities.objects.all()
    # for f in files:
    # print(f)

    return render(request, 'universities/international_universities.html', {'universities': universities})

