
"""Membership URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from membership import views

urlpatterns = [
    url(r'^home$', views.home, name='home'),
    url(r'^premium_membership$', views.premium_membership, name='premium_membership'),
    url(r'^basic_form1_exams$', views.basic_form1_exams, name='basic_form1_exams'),
    url(r'^basic_form2_exams$', views.basic_form2_exams, name='basic_form2_exams'),
    url(r'^basic_form3_exams$', views.basic_form3_exams, name='basic_form3_exams'),
    url(r'^basic_form4_exams$', views.basic_form4_exams, name='basic_form4_exams'),
    url(r'^form1_cat1$', views.form1_cat1, name='form1_cat1'),
    url(r'^form1_cat2$', views.form1_cat2, name='form1_cat2'),
    url(r'^form1_cat3$', views.form1_cat3, name='form1_cat3'),
    url(r'^form1_end_term$', views.form1_end_term, name='form1_end_term'),
    url(r'^form2_cat1$', views.form2_cat1, name='form2_cat1'),
    url(r'^form2_cat2$', views.form2_cat2, name='form2_cat2'),
    url(r'^form2_cat3$', views.form2_cat3, name='form2_cat3'),
    url(r'^form2_end_term$', views.form2_end_term, name='form2_end_term'),
    url(r'^form3_cat1$', views.form3_cat1, name='form3_cat1'),
    url(r'^form3_cat2$', views.form3_cat2, name='form3_cat2'),
    url(r'^form3_cat3$', views.form3_cat3, name='form3_cat3'),
    url(r'^form3_end_term$', views.form3_end_term, name='form3_end_term'),
    url(r'^form4_mock1$', views.form4_mock1, name='form4_mock1'),
    url(r'^form4_mock2$', views.form4_mock2, name='form4_mock2'),
    url(r'^form4_mock3$', views.form4_mock3, name='form4_mock3'),
    url(r'^form4_revision$', views.form4_revision, name='form4_revision'),
]
