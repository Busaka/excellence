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

    return render(request, 'universities/universities.html', {})

def local_universities(request):
    """TODO: Docstring for home.
    :returns: TODO

    """
    local_universities  = LocalUniversities.objects.all()
    # for f in files:
    # print(f)

    return render(request, 'universities/local_universities.html', {'local_universities': local_universities})

def local_university_details(request, uni_id):
    """TODO: Docstring for home.
    :returns: TODO

    """
    local_university_details  = LocalUniversities.objects.get(pk=uni_id)
    # for f in local_university_details:
    # print('LOCAL_UNI_ID', local_university_details)

    return render(request, 'universities/local_uni_details.html', {'local_university_details': local_university_details})

def international_universities(request):
    """TODO: Docstring for home.
    :returns: TODO

    """
    intern_universities = InternationalUniversities.objects.all()
    # for f in files:
    # print(f)

    return render(request, 'universities/international_universities.html', {'intern_universities': intern_universities})

def international_uni_details(request, uni_id):
    """TODO: Docstring for home.
    :returns: TODO

    """
    international_uni_details  = InternationalUniversities.objects.get(pk=uni_id)
    # for f in local_university_details:
    # print('LOCAL_UNI_ID', local_university_details)

    return render(request, 'universities/international_uni_details.html', {'international_uni_details': international_uni_details})
