from django.shortcuts import render
from . import models

# Create your views here.

def home(request):
    """TODO: Docstring for home.
    :returns: TODO

    """
    return render(request, 'membership/membership.html')

# Basic services

def basic_form1_exams(request):
    """TODO: Docstring for home.
    :returns: TODO

    """
    form1 = models.BasicForm1Exam.objects.all()
    return render(request, 'membership/basic_form1_exams.html', { 'form1': form1 })

def basic_form2_exams(request):
    """TODO: Docstring for home.
    :returns: TODO

    """
    form2 = models.BasicForm2Exam.objects.all()
    return render(request, 'membership/basic_form2_exams.html', { 'form2': form2 })

def basic_form3_exams(request):
    """TODO: Docstring for home.
    :returns: TODO

    """
    form3 = models.BasicForm3Exam.objects.all()
    return render(request, 'membership/basic_form3_exams.html', { 'form3': form3 })

def basic_form4_exams(request):
    """TODO: Docstring for home.
    :returns: TODO

    """
    form4 = models.BasicForm4Exam.objects.all()
    return render(request, 'membership/basic_form4_exams.html', { 'form4': form4 })


########################################################################################
# Form One Premium services
########################################################################################

def premium_membership(request):
    """TODO: Docstring for home.
    :returns: TODO

    """
    return render(request, 'membership/premium_membership.html', {})

def form1_cat1(request):
    """TODO: Docstring for home.
    :returns: TODO

    """
    form1_cat1 = models.Form1Cat1.objects.all()
    return render(request, 'membership/form1_cat1.html', { 'form1_cat1': form1_cat1 })
def form1_cat2(request):
    """TODO: Docstring for home.
    :returns: TODO

    """
    form1_cat2 = models.Form1Cat2.objects.all()
    return render(request, 'membership/form1_cat2.html', { 'form1_cat2': form1_cat2 })
def form1_cat3(request):
    """TODO: Docstring for home.
    :returns: TODO

    """
    form1_cat3 = models.Form1Cat3.objects.all()
    return render(request, 'membership/form1_cat3.html', { 'form1_cat3': form1_cat3 })
def form1_end_term(request):
    """TODO: Docstring for home.
    :returns: TODO

    """
    form1_end_term = models.Form1EndTerm.objects.all()
    return render(request, 'membership/form1_end_term.html', { 'form1_end_term': form1_end_term })

########################################################################################
# Form Two Premium services
########################################################################################

def form2_cat1(request):
    """TODO: Docstring for home.
    :returns: TODO

    """
    form2_cat1 = models.Form2Cat1.objects.all()
    return render(request, 'membership/form2_cat1.html', { 'form2_cat1': form2_cat1 })
def form2_cat2(request):
    """TODO: Docstring for home.
    :returns: TODO

    """
    form2_cat2 = models.Form2Cat2.objects.all()
    return render(request, 'membership/form2_cat2.html', { 'form2_cat2': form2_cat2 })
def form2_cat3(request):
    """TODO: Docstring for home.
    :returns: TODO

    """
    form2_cat3 = models.Form2Cat3.objects.all()
    return render(request, 'membership/form2_cat3.html', { 'form2_cat3': form2_cat3 })
def form2_end_term(request):
    """TODO: Docstring for home.
    :returns: TODO

    """
    form2_end_term = models.Form2EndTerm.objects.all()
    return render(request, 'membership/form2_end_term.html', { 'form2_end_term': form2_end_term })

########################################################################################
# Form Three Premium services
########################################################################################

def form3_cat1(request):
    """TODO: Docstring for home.
    :returns: TODO

    """
    form3_cat1 = models.Form3Cat1.objects.all()
    return render(request, 'membership/form3_cat1.html', { 'form3_cat1': form3_cat1 })
def form3_cat2(request):
    """TODO: Docstring for home.
    :returns: TODO

    """
    form3_cat2 = Form3Cat2.objects.all()
    return render(request, 'membership/form3_cat2.html', { 'form3_cat2': form3_cat2 })
def form3_cat3(request):
    """TODO: Docstring for home.
    :returns: TODO

    """
    form3_cat3 = models.Form3Cat3.objects.all()
    return render(request, 'membership/form3_cat3.html', { 'form3_cat3': form3_cat3 })
def form3_end_term(request):
    """TODO: Docstring for home.
    :returns: TODO

    """
    form3_end_term = models.Form3EndTerm.objects.all()
    return render(request, 'membership/form3_end_term.html', { 'form3_end_term': form3_end_term })

########################################################################################
# Form Four Premium services
########################################################################################

def form4_mock1(request):
    """TODO: Docstring for home.
    :returns: TODO

    """
    form4_mock1 = models.Form4Mock1.objects.all()
    return render(request, 'membership/form4_mock1.html', { 'form4_mock1': form4_mock1 })
def form4_mock2(request):
    """TODO: Docstring for home.
    :returns: TODO

    """
    form4_mock2 = models.Form4Mock2.objects.all()
    return render(request, 'membership/form4_mock2.html', { 'form4_mock2': form4_mock2 })
def form4_mock3(request):
    """TODO: Docstring for home.
    :returns: TODO

    """
    form4_mock3 = models.Form4Mock3.objects.all()
    return render(request, 'membership/form4_mock3.html', { 'form4_mock3': form4_mock3 })
def form4_revision(request):
    """TODO: Docstring for home.
    :returns: TODO

    """
    form4_revision = models.Form4Revision.objects.all()
    return render(request, 'membership/form4_revision.html', { 'form4_revision': form4_revision })
