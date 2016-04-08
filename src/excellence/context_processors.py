from itertools import chain
from operator import attrgetter
from colleges.models import College
from universities.models import LocalUniversities
from universities.models import InternationalUniversities
from membership.models import (
        BasicForm1Exam,
        BasicForm2Exam,
        BasicForm3Exam,
        BasicForm4Exam,
        StudyTip,
        )


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
    study_tips = StudyTip.objects.all()
    form1 = BasicForm1Exam.objects.all()
    form2 = BasicForm2Exam.objects.all()
    form3 = BasicForm3Exam.objects.all()
    form4 = BasicForm4Exam.objects.all()
        
    return {
            'featured_colleges': featured_colleges, 
            'featured_local_uni': featured_local_uni, 
            'featured_inter_uni': featured_inter_uni,
            'study_tips': study_tips,
            }
