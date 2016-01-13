from django.views.generic.base import TemplateView
from high_schools.models import HighSchool
from colleges.models import College


class HomePage(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        schools = HighSchool.objects.filter(featured='yes').order_by('?')[:4]
        colleges = College.objects.all().order_by('?')
        context['schools'] = schools
        context['colleges'] = colleges
        return context


class AboutPage(TemplateView):
    template_name = "about.html"
