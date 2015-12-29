from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.


def magazine(request):
    """TODO: Docstring for home.
    :returns: TODO
    """
    return render(request, 'magazine/magazine.html', {})

