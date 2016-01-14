from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Article

# Create your views here.


def magazine(request):
    """TODO: Docstring for home.
    :returns: TODO
    """
    articles = Article.objects.get(pk=1)
    return render(request, 'magazine/magazine.html', {'articles': articles})

