from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Article

# Create your views here.


def magazine(request):
    """TODO: Docstring for home.
    :returns: TODO
    """
    try:
        articles = Article.objects.get(pk=1)
    except:
        articles = Article.objects.all()
    return render(request, 'magazine/magazine.html', {'articles': articles})

