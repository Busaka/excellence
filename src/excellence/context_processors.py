from itertools import chain
from operator import attrgetter
from colleges.models import College
from universities.models import LocalUniversities
from universities.models import InternationalUniversities
from membership import models 

# def featured_institutions(request):

#     featured_colleges = College.objects.filter(featured='yes').order_by('?')
#     featured_local_uni = LocalUniversities.objects.filter(featured='yes').order_by('?')
#     featured_inter_uni = InternationalUniversities.objects.filter(featured='yes').order_by('?')
#     featured_colle_uni = sorted(chain(featured_colleges, featured_local_uni), key=attrgetter('published'))
        
#     return {'featured_colleges': featured_colleges, 'featured_local_uni': featured_local_uni, 'featured_inter_uni': featured_inter_uni}

def featured_institutions(request):

    featured_colleges = College.objects.filter(featured='yes').order_by('?')
    featured_local_uni = LocalUniversities.objects.filter(featured='yes').order_by('?')
    featured_inter_uni = InternationalUniversities.objects.filter(featured='yes').order_by('?')
    basic_study_tips = models.BasicStudyTip.objects.all()
    premium_study_tips = models.PremiumStudyTip.objects.all()
        
    return {
            'featured_colleges': featured_colleges, 
            'featured_local_uni': featured_local_uni, 
            'featured_inter_uni': featured_inter_uni,
            'basic_study_tips': basic_study_tips,
            'premium_study_tips': premium_study_tips,
            }
