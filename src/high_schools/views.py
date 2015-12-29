from django.shortcuts import render
from .models import HighSchool

# Create your views here.


def home(request):
    """TODO: Docstring for home.
    :returns: TODO

    """
    files = HighSchool.objects.all()
    # for f in files:
    # print(f)

    return render(request, 'high_schools/home.html', {'files': files})

