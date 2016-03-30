from django.shortcuts import render

# Create your views here.

def home(request):
    """TODO: Docstring for home.
    :returns: TODO

    """
    return render(request, 'membership/membership.html')

def basic(request):
    """TODO: Docstring for home.
    :returns: TODO

    """
    return render(request, 'membership/basic_membership.html')

def premium(request):
    """TODO: Docstring for home.
    :returns: TODO

    """
    return render(request, 'membership/premium_membership.html')
