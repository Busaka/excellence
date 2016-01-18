from colleges.models import College
from universities.models import LocalUniversities


def featured_institutions(request):
    featured_colleges = College.objects.all().order_by('?')
    featured_universities = LocalUniversities.objects.all().order_by('?')
    return {'featured_colleges': featured_colleges, 'featured_universities': featured_universities}
