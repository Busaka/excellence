from django.shortcuts import render
from excellence_profile.models import (
                                        ExcellenceAbout, 
                                        TermsAndCondition,
                                        ExcellenceCopyright,
                                        )

# Create your views here.
def excellence_about(request):
    abouts = ExcellenceAbout.objects.all()
    return render(request, 'excellence_profile/excellence_about.html', {'abouts': abouts})

def terms_conditions(request):
    terms_conditions = TermsAndCondition.objects.all()
    return render(request, 'excellence_profile/terms_and_conditions.html',
            {'terms_conditions': terms_conditions })

def excellence_copyright(request):
    excellence_copyrights = ExcellenceCopyright.objects.all()
    return render(request, 'excellence_profile/excellence_copyright.html',
            {'excellence_copyrights': excellence_copyrights })
