from django.contrib import admin
from excellence_profile.models import (
                                        ExcellenceAbout, 
                                        TermsAndCondition,
                                        ExcellenceCopyright,
                                        )
# Register your models here.
admin.site.register(ExcellenceAbout)
admin.site.register(TermsAndCondition)
admin.site.register(ExcellenceCopyright)

