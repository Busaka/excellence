from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.



class News(TemplateView):
    template_name = "news/news.html"
    # def get_context_data(self, **kwargs):
    #     context = super(HomePage, self).get_context_data(**kwargs)
    #     context['schools'] = HighSchool.objects.all()[:4]
    #     return context
