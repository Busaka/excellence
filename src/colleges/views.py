from django.shortcuts import render

# Create your views here.


def home(request):
    """TODO: Docstring for home.
    :returns: TODO

    """
    return render(request, 'colleges/colleges.html', {})

