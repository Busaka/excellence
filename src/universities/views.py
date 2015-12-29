from django.shortcuts import render

from .models import University

# Create your views here.


def home(request):
    """TODO: Docstring for home.
    :returns: TODO

    """
    files = University.objects.all()
    # for f in files:
    # print(f)

    return render(request, 'universities/universities.html', {'files': files})

