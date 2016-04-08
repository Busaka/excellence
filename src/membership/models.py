from __future__ import unicode_literals
from django.db import models


class StudyTip(models.Model):
    tip1 = models.CharField("Study Tip One", max_length=200, blank=True, null=True)
    tip2 = models.CharField("Study Tip Two", max_length=200, blank=True, null=True)
    tip3 = models.CharField("Study Tip Three", max_length=200, blank=True, null=True)
    tip4 = models.CharField("Study Tip Four", max_length=200, blank=True, null=True)
    tip5 = models.CharField("Study Tip Five", max_length=200, blank=True, null=True)
    tip6 = models.CharField("Study Tip Six", max_length=200, blank=True, null=True)
    tip7 = models.CharField("Study Tip Seven", max_length=200, blank=True, null=True)
    tip8 = models.CharField("Study Tip Eight", max_length=200, blank=True, null=True)
    tip9 = models.CharField("Study Tip Nine", max_length=200, blank=True, null=True)
    tip10 = models.CharField("Study Tip Ten", max_length=200, blank=True, null=True)
    tip11 = models.CharField("Study Tip Eleven", max_length=200, blank=True, null=True)
    tip12 = models.CharField("Study Tip Twelve", max_length=200, blank=True, null=True)
    tip13 = models.CharField("Study Tip Thirteen", max_length=200, blank=True, null=True)
    tip14 = models.CharField("Study Tip Fourteen", max_length=200, blank=True, null=True)
    tip15 = models.CharField("Study Tip Fifteen", max_length=200, blank=True, null=True)

    def __str__(self):
        return 'Study Tips'


class BasicForm1Exam(models.Model):
    subject1 = models.CharField("Subject One", max_length=200, blank=True, null=True)
    subject1_code = models.FileField("Subject One Code",upload_to='membership/form_one/subjects', max_length=200, blank=True, null=True)
    subject2 = models.CharField("Subject Two", max_length=200, blank=True, null=True)
    subject2_code = models.FileField("Subject  Two Code",upload_to='membership/form_one/subjects', max_length=200, blank=True, null=True)
    subject3 = models.CharField("Subject Three", max_length=200, blank=True, null=True)
    subject3_code = models.FileField("Subject Three Code",upload_to='membership/form_one/subjects', max_length=200, blank=True, null=True)
    subject4 = models.CharField("Subject Four", max_length=200, blank=True, null=True)
    subject4_code = models.FileField("Subject Four Code",upload_to='membership/form_one/subjects', max_length=200, blank=True, null=True)
    subject5 = models.CharField("Subject Five", max_length=200, blank=True, null=True)
    subject5_code = models.FileField("Subject Five Code",upload_to='membership/form_one/subjects', max_length=200, blank=True, null=True)
    subject6 = models.CharField("Subject Six", max_length=200, blank=True, null=True)
    subject6_code = models.FileField("Subject Six Code",upload_to='membership/form_one/subjects', max_length=200, blank=True, null=True)
    subject7 = models.CharField("Subject Seven", max_length=200, blank=True, null=True)
    subject7_code = models.FileField("Subject Seven Code",upload_to='membership/form_one/subjects', max_length=200, blank=True, null=True)
    subject8 = models.CharField("Subject Eight", max_length=200, blank=True, null=True)
    subject8_code = models.FileField("Subject Eight Code",upload_to='membership/form_one/subjects', max_length=200, blank=True, null=True)
    subject9 = models.CharField("Subject Nine", max_length=200, blank=True, null=True)
    subject9_code = models.FileField("Subject Nine Code",upload_to='membership/form_one/subjects', max_length=200, blank=True, null=True)
    subject10 = models.CharField("Subject Ten", max_length=200, blank=True, null=True)
    subject10_code = models.FileField("Subject Ten Code",upload_to='membership/form_one/subjects', max_length=200, blank=True, null=True)
    subject11 = models.CharField("Subject Eleven", max_length=200, blank=True, null=True)
    subject11_code = models.FileField("Subject Eleven Code",upload_to='membership/form_one/subjects', max_length=200, blank=True, null=True)
    subject12 = models.CharField("Subject Twelve", max_length=200, blank=True, null=True)
    subject12_code = models.FileField("Subject Twelve Code",upload_to='membership/form_one/subjects', max_length=200, blank=True, null=True)
    subject13 = models.CharField("Subject Thirteen", max_length=200, blank=True, null=True)
    subject13_code = models.FileField("Subject Thirteen Code",upload_to='membership/form_one/subjects', max_length=200, blank=True, null=True)
    subject14 = models.CharField("Subject Fourteen", max_length=200, blank=True, null=True)
    subject14_code = models.FileField("Subject Fourteen Code",upload_to='membership/form_one/subjects', max_length=200, blank=True, null=True)
    subject15 = models.CharField("Subject Fifteen", max_length=200, blank=True, null=True)
    subject15_code = models.FileField("Subject Fifteen  Code",upload_to='membership/form_one/subjects', max_length=200, blank=True, null=True)

    def __str__(self):
        return 'Basic Form One Exams'


class BasicForm2Exam(models.Model):
    subject1 = models.CharField("Subject One", max_length=200, blank=True, null=True)
    subject1_code = models.FileField("Subject One Code",upload_to='membership/form_two/subjects', max_length=200, blank=True, null=True)
    subject2 = models.CharField("Subject Two", max_length=200, blank=True, null=True)
    subject2_code = models.FileField("Subject  Two Code",upload_to='membership/form_two/subjects', max_length=200, blank=True, null=True)
    subject3 = models.CharField("Subject Three", max_length=200, blank=True, null=True)
    subject3_code = models.FileField("Subject Three Code",upload_to='membership/form_two/subjects', max_length=200, blank=True, null=True)
    subject4 = models.CharField("Subject Four", max_length=200, blank=True, null=True)
    subject4_code = models.FileField("Subject Four Code",upload_to='membership/form_two/subjects', max_length=200, blank=True, null=True)
    subject5 = models.CharField("Subject Five", max_length=200, blank=True, null=True)
    subject5_code = models.FileField("Subject Five Code",upload_to='membership/form_two/subjects', max_length=200, blank=True, null=True)
    subject6 = models.CharField("Subject Six", max_length=200, blank=True, null=True)
    subject6_code = models.FileField("Subject Six Code",upload_to='membership/form_two/subjects', max_length=200, blank=True, null=True)
    subject7 = models.CharField("Subject Seven", max_length=200, blank=True, null=True)
    subject7_code = models.FileField("Subject Seven Code",upload_to='membership/form_two/subjects', max_length=200, blank=True, null=True)
    subject8 = models.CharField("Subject Eight", max_length=200, blank=True, null=True)
    subject8_code = models.FileField("Subject Eight Code",upload_to='membership/form_two/subjects', max_length=200, blank=True, null=True)
    subject9 = models.CharField("Subject Nine", max_length=200, blank=True, null=True)
    subject9_code = models.FileField("Subject Nine Code",upload_to='membership/form_two/subjects', max_length=200, blank=True, null=True)
    subject10 = models.CharField("Subject Ten", max_length=200, blank=True, null=True)
    subject10_code = models.FileField("Subject Ten Code",upload_to='membership/form_two/subjects', max_length=200, blank=True, null=True)
    subject11 = models.CharField("Subject Eleven", max_length=200, blank=True, null=True)
    subject11_code = models.FileField("Subject Eleven Code",upload_to='membership/form_two/subjects', max_length=200, blank=True, null=True)
    subject12 = models.CharField("Subject Twelve", max_length=200, blank=True, null=True)
    subject12_code = models.FileField("Subject Twelve Code",upload_to='membership/form_two/subjects', max_length=200, blank=True, null=True)
    subject13 = models.CharField("Subject Thirteen", max_length=200, blank=True, null=True)
    subject13_code = models.FileField("Subject Thirteen Code",upload_to='membership/form_two/subjects', max_length=200, blank=True, null=True)
    subject14 = models.CharField("Subject Fourteen", max_length=200, blank=True, null=True)
    subject14_code = models.FileField("Subject Fourteen Code",upload_to='membership/form_two/subjects', max_length=200, blank=True, null=True)
    subject15 = models.CharField("Subject Fifteen", max_length=200, blank=True, null=True)
    subject15_code = models.FileField("Subject Fifteen  Code",upload_to='membership/form_two/subjects', max_length=200, blank=True, null=True)

    def __str__(self):
        return 'Basic Form Two Exams'


class BasicForm3Exam(models.Model):
    subject1 = models.CharField("Subject One", max_length=200, blank=True, null=True)
    subject1_code = models.FileField("Subject One Code",upload_to='membership/form_three/subjects', max_length=200, blank=True, null=True)
    subject2 = models.CharField("Subject Two", max_length=200, blank=True, null=True)
    subject2_code = models.FileField("Subject  Two Code",upload_to='membership/form_three/subjects', max_length=200, blank=True, null=True)
    subject3 = models.CharField("Subject Three", max_length=200, blank=True, null=True)
    subject3_code = models.FileField("Subject Three Code",upload_to='membership/form_three/subjects', max_length=200, blank=True, null=True)
    subject4 = models.CharField("Subject Four", max_length=200, blank=True, null=True)
    subject4_code = models.FileField("Subject Four Code",upload_to='membership/form_three/subjects', max_length=200, blank=True, null=True)
    subject5 = models.CharField("Subject Five", max_length=200, blank=True, null=True)
    subject5_code = models.FileField("Subject Five Code",upload_to='membership/form_three/subjects', max_length=200, blank=True, null=True)
    subject6 = models.CharField("Subject Six", max_length=200, blank=True, null=True)
    subject6_code = models.FileField("Subject Six Code",upload_to='membership/form_three/subjects', max_length=200, blank=True, null=True)
    subject7 = models.CharField("Subject Seven", max_length=200, blank=True, null=True)
    subject7_code = models.FileField("Subject Seven Code",upload_to='membership/form_three/subjects', max_length=200, blank=True, null=True)
    subject8 = models.CharField("Subject Eight", max_length=200, blank=True, null=True)
    subject8_code = models.FileField("Subject Eight Code",upload_to='membership/form_three/subjects', max_length=200, blank=True, null=True)
    subject9 = models.CharField("Subject Nine", max_length=200, blank=True, null=True)
    subject9_code = models.FileField("Subject Nine Code",upload_to='membership/form_three/subjects', max_length=200, blank=True, null=True)
    subject10 = models.CharField("Subject Ten", max_length=200, blank=True, null=True)
    subject10_code = models.FileField("Subject Ten Code",upload_to='membership/form_three/subjects', max_length=200, blank=True, null=True)
    subject11 = models.CharField("Subject Eleven", max_length=200, blank=True, null=True)
    subject11_code = models.FileField("Subject Eleven Code",upload_to='membership/form_three/subjects', max_length=200, blank=True, null=True)
    subject12 = models.CharField("Subject Twelve", max_length=200, blank=True, null=True)
    subject12_code = models.FileField("Subject Twelve Code",upload_to='membership/form_three/subjects', max_length=200, blank=True, null=True)
    subject13 = models.CharField("Subject Thirteen", max_length=200, blank=True, null=True)
    subject13_code = models.FileField("Subject Thirteen Code",upload_to='membership/form_three/subjects', max_length=200, blank=True, null=True)
    subject14 = models.CharField("Subject Fourteen", max_length=200, blank=True, null=True)
    subject14_code = models.FileField("Subject Fourteen Code",upload_to='membership/form_three/subjects', max_length=200, blank=True, null=True)
    subject15 = models.CharField("Subject Fifteen", max_length=200, blank=True, null=True)
    subject15_code = models.FileField("Subject Fifteen  Code",upload_to='membership/form_three/subjects', max_length=200, blank=True, null=True)

    def __str__(self):
        return 'Basic Form Three Exams'


class BasicForm4Exam(models.Model):
    subject1 = models.CharField("Subject One", max_length=200, blank=True, null=True)
    subject1_code = models.FileField("Subject One Code",upload_to='membership/form_four/subjects', max_length=200, blank=True, null=True)
    subject2 = models.CharField("Subject Two", max_length=200, blank=True, null=True)
    subject2_code = models.FileField("Subject  Two Code",upload_to='membership/form_four/subjects', max_length=200, blank=True, null=True)
    subject3 = models.CharField("Subject Three", max_length=200, blank=True, null=True)
    subject3_code = models.FileField("Subject Three Code",upload_to='membership/form_four/subjects', max_length=200, blank=True, null=True)
    subject4 = models.CharField("Subject Four", max_length=200, blank=True, null=True)
    subject4_code = models.FileField("Subject Four Code",upload_to='membership/form_four/subjects', max_length=200, blank=True, null=True)
    subject5 = models.CharField("Subject Five", max_length=200, blank=True, null=True)
    subject5_code = models.FileField("Subject Five Code",upload_to='membership/form_four/subjects', max_length=200, blank=True, null=True)
    subject6 = models.CharField("Subject Six", max_length=200, blank=True, null=True)
    subject6_code = models.FileField("Subject Six Code",upload_to='membership/form_four/subjects', max_length=200, blank=True, null=True)
    subject7 = models.CharField("Subject Seven", max_length=200, blank=True, null=True)
    subject7_code = models.FileField("Subject Seven Code",upload_to='membership/form_four/subjects', max_length=200, blank=True, null=True)
    subject8 = models.CharField("Subject Eight", max_length=200, blank=True, null=True)
    subject8_code = models.FileField("Subject Eight Code",upload_to='membership/form_four/subjects', max_length=200, blank=True, null=True)
    subject9 = models.CharField("Subject Nine", max_length=200, blank=True, null=True)
    subject9_code = models.FileField("Subject Nine Code",upload_to='membership/form_four/subjects', max_length=200, blank=True, null=True)
    subject10 = models.CharField("Subject Ten", max_length=200, blank=True, null=True)
    subject10_code = models.FileField("Subject Ten Code",upload_to='membership/form_four/subjects', max_length=200, blank=True, null=True)
    subject11 = models.CharField("Subject Eleven", max_length=200, blank=True, null=True)
    subject11_code = models.FileField("Subject Eleven Code",upload_to='membership/form_four/subjects', max_length=200, blank=True, null=True)
    subject12 = models.CharField("Subject Twelve", max_length=200, blank=True, null=True)
    subject12_code = models.FileField("Subject Twelve Code",upload_to='membership/form_four/subjects', max_length=200, blank=True, null=True)
    subject13 = models.CharField("Subject Thirteen", max_length=200, blank=True, null=True)
    subject13_code = models.FileField("Subject Thirteen Code",upload_to='membership/form_four/subjects', max_length=200, blank=True, null=True)
    subject14 = models.CharField("Subject Fourteen", max_length=200, blank=True, null=True)
    subject14_code = models.FileField("Subject Fourteen Code",upload_to='membership/form_four/subjects', max_length=200, blank=True, null=True)
    subject15 = models.CharField("Subject Fifteen", max_length=200, blank=True, null=True)
    subject15_code = models.FileField("Subject Fifteen  Code",upload_to='membership/form_four/subjects', max_length=200, blank=True, null=True)

    def __str__(self):
        return 'Basic Form Four Exams'


##########################################################################################################################
                                            # PREMIUM SERVICES
########################################################################################################################## # FORM ONE
# ########################################################################################################################


class Form1Cat1(models.Model):
    subject1 = models.CharField("Subject One", max_length=200, blank=True, null=True)
    subject1_code = models.FileField("Subject One Code",upload_to='membership/form1_cat1/subjects', max_length=200, blank=True, null=True)
    subject2 = models.CharField("Subject Two", max_length=200, blank=True, null=True)
    subject2_code = models.FileField("Subject  Two Code",upload_to='membership/form1_cat1/subjects', max_length=200, blank=True, null=True)
    subject3 = models.CharField("Subject Three", max_length=200, blank=True, null=True)
    subject3_code = models.FileField("Subject Three Code",upload_to='membership/form1_cat1/subjects', max_length=200, blank=True, null=True)
    subject4 = models.CharField("Subject Four", max_length=200, blank=True, null=True)
    subject4_code = models.FileField("Subject Four Code",upload_to='membership/form1_cat1/subjects', max_length=200, blank=True, null=True)
    subject5 = models.CharField("Subject Five", max_length=200, blank=True, null=True)
    subject5_code = models.FileField("Subject Five Code",upload_to='membership/form1_cat1/subjects', max_length=200, blank=True, null=True)
    subject6 = models.CharField("Subject Six", max_length=200, blank=True, null=True)
    subject6_code = models.FileField("Subject Six Code",upload_to='membership/form1_cat1/subjects', max_length=200, blank=True, null=True)
    subject7 = models.CharField("Subject Seven", max_length=200, blank=True, null=True)
    subject7_code = models.FileField("Subject Seven Code",upload_to='membership/form1_cat1/subjects', max_length=200, blank=True, null=True)
    subject8 = models.CharField("Subject Eight", max_length=200, blank=True, null=True)
    subject8_code = models.FileField("Subject Eight Code",upload_to='membership/form1_cat1/subjects', max_length=200, blank=True, null=True)
    subject9 = models.CharField("Subject Nine", max_length=200, blank=True, null=True)
    subject9_code = models.FileField("Subject Nine Code",upload_to='membership/form1_cat1/subjects', max_length=200, blank=True, null=True)
    subject10 = models.CharField("Subject Ten", max_length=200, blank=True, null=True)
    subject10_code = models.FileField("Subject Ten Code",upload_to='membership/form1_cat1/subjects', max_length=200, blank=True, null=True)
    subject11 = models.CharField("Subject Eleven", max_length=200, blank=True, null=True)
    subject11_code = models.FileField("Subject Eleven Code",upload_to='membership/form1_cat1/subjects', max_length=200, blank=True, null=True)
    subject12 = models.CharField("Subject Twelve", max_length=200, blank=True, null=True)
    subject12_code = models.FileField("Subject Twelve Code",upload_to='membership/form1_cat1/subjects', max_length=200, blank=True, null=True)
    subject13 = models.CharField("Subject Thirteen", max_length=200, blank=True, null=True)
    subject13_code = models.FileField("Subject Thirteen Code",upload_to='membership/form1_cat1/subjects', max_length=200, blank=True, null=True)
    subject14 = models.CharField("Subject Fourteen", max_length=200, blank=True, null=True)
    subject14_code = models.FileField("Subject Fourteen Code",upload_to='membership/form1_cat1/subjects', max_length=200, blank=True, null=True)
    subject15 = models.CharField("Subject Fifteen", max_length=200, blank=True, null=True)
    subject15_code = models.FileField("Subject Fifteen Code",upload_to='membership/form1_cat1/subjects', max_length=200, blank=True, null=True)

    def __str__(self):
        return 'Form One CAT1'


class Form1Cat2(models.Model):
    subject1 = models.CharField("Subject One", max_length=200, blank=True, null=True)
    subject1_code = models.FileField("Subject One Code",upload_to='membership/form1_cat2/subjects', max_length=200, blank=True, null=True)
    subject2 = models.CharField("Subject Two", max_length=200, blank=True, null=True)
    subject2_code = models.FileField("Subject  Two Code",upload_to='membership/form1_cat2/subjects', max_length=200, blank=True, null=True)
    subject3 = models.CharField("Subject Three", max_length=200, blank=True, null=True)
    subject3_code = models.FileField("Subject Three Code",upload_to='membership/form1_cat2/subjects', max_length=200, blank=True, null=True)
    subject4 = models.CharField("Subject Four", max_length=200, blank=True, null=True)
    subject4_code = models.FileField("Subject Four Code",upload_to='membership/form1_cat2/subjects', max_length=200, blank=True, null=True)
    subject5 = models.CharField("Subject Five", max_length=200, blank=True, null=True)
    subject5_code = models.FileField("Subject Five Code",upload_to='membership/form1_cat2/subjects', max_length=200, blank=True, null=True)
    subject6 = models.CharField("Subject Six", max_length=200, blank=True, null=True)
    subject6_code = models.FileField("Subject Six Code",upload_to='membership/form1_cat2/subjects', max_length=200, blank=True, null=True)
    subject7 = models.CharField("Subject Seven", max_length=200, blank=True, null=True)
    subject7_code = models.FileField("Subject Seven Code",upload_to='membership/form1_cat2/subjects', max_length=200, blank=True, null=True)
    subject8 = models.CharField("Subject Eight", max_length=200, blank=True, null=True)
    subject8_code = models.FileField("Subject Eight Code",upload_to='membership/form1_cat2/subjects', max_length=200, blank=True, null=True)
    subject9 = models.CharField("Subject Nine", max_length=200, blank=True, null=True)
    subject9_code = models.FileField("Subject Nine Code",upload_to='membership/form1_cat2/subjects', max_length=200, blank=True, null=True)
    subject10 = models.CharField("Subject Ten", max_length=200, blank=True, null=True)
    subject10_code = models.FileField("Subject Ten Code",upload_to='membership/form1_cat2/subjects', max_length=200, blank=True, null=True)
    subject11 = models.CharField("Subject Eleven", max_length=200, blank=True, null=True)
    subject11_code = models.FileField("Subject Eleven Code",upload_to='membership/form1_cat2/subjects', max_length=200, blank=True, null=True)
    subject12 = models.CharField("Subject Twelve", max_length=200, blank=True, null=True)
    subject12_code = models.FileField("Subject Twelve Code",upload_to='membership/form1_cat2/subjects', max_length=200, blank=True, null=True)
    subject13 = models.CharField("Subject Thirteen", max_length=200, blank=True, null=True)
    subject13_code = models.FileField("Subject Thirteen Code",upload_to='membership/form1_cat2/subjects', max_length=200, blank=True, null=True)
    subject14 = models.CharField("Subject Fourteen", max_length=200, blank=True, null=True)
    subject14_code = models.FileField("Subject Fourteen Code",upload_to='membership/form1_cat2/subjects', max_length=200, blank=True, null=True)
    subject15 = models.CharField("Subject Fifteen", max_length=200, blank=True, null=True)
    subject15_code = models.FileField("Subject Fifteen Code",upload_to='membership/form1_cat2/subjects', max_length=200, blank=True, null=True)

    def __str__(self):
        return 'Form One CAT2'


class Form1Cat3(models.Model):
    subject1 = models.CharField("Subject One", max_length=200, blank=True, null=True)
    subject1_code = models.FileField("Subject One Code",upload_to='membership/form1_cat3/subjects', max_length=200, blank=True, null=True)
    subject2 = models.CharField("Subject Two", max_length=200, blank=True, null=True)
    subject2_code = models.FileField("Subject  Two Code",upload_to='membership/form1_cat3/subjects', max_length=200, blank=True, null=True)
    subject3 = models.CharField("Subject Three", max_length=200, blank=True, null=True)
    subject3_code = models.FileField("Subject Three Code",upload_to='membership/form1_cat3/subjects', max_length=200, blank=True, null=True)
    subject4 = models.CharField("Subject Four", max_length=200, blank=True, null=True)
    subject4_code = models.FileField("Subject Four Code",upload_to='membership/form1_cat3/subjects', max_length=200, blank=True, null=True)
    subject5 = models.CharField("Subject Five", max_length=200, blank=True, null=True)
    subject5_code = models.FileField("Subject Five Code",upload_to='membership/form1_cat3/subjects', max_length=200, blank=True, null=True)
    subject6 = models.CharField("Subject Six", max_length=200, blank=True, null=True)
    subject6_code = models.FileField("Subject Six Code",upload_to='membership/form1_cat3/subjects', max_length=200, blank=True, null=True)
    subject7 = models.CharField("Subject Seven", max_length=200, blank=True, null=True)
    subject7_code = models.FileField("Subject Seven Code",upload_to='membership/form1_cat3/subjects', max_length=200, blank=True, null=True)
    subject8 = models.CharField("Subject Eight", max_length=200, blank=True, null=True)
    subject8_code = models.FileField("Subject Eight Code",upload_to='membership/form1_cat3/subjects', max_length=200, blank=True, null=True)
    subject9 = models.CharField("Subject Nine", max_length=200, blank=True, null=True)
    subject9_code = models.FileField("Subject Nine Code",upload_to='membership/form1_cat3/subjects', max_length=200, blank=True, null=True)
    subject10 = models.CharField("Subject Ten", max_length=200, blank=True, null=True)
    subject10_code = models.FileField("Subject Ten Code",upload_to='membership/form1_cat3/subjects', max_length=200, blank=True, null=True)
    subject11 = models.CharField("Subject Eleven", max_length=200, blank=True, null=True)
    subject11_code = models.FileField("Subject Eleven Code",upload_to='membership/form1_cat3/subjects', max_length=200, blank=True, null=True)
    subject12 = models.CharField("Subject Twelve", max_length=200, blank=True, null=True)
    subject12_code = models.FileField("Subject Twelve Code",upload_to='membership/form1_cat3/subjects', max_length=200, blank=True, null=True)
    subject13 = models.CharField("Subject Thirteen", max_length=200, blank=True, null=True)
    subject13_code = models.FileField("Subject Thirteen Code",upload_to='membership/form1_cat3/subjects', max_length=200, blank=True, null=True)
    subject14 = models.CharField("Subject Fourteen", max_length=200, blank=True, null=True)
    subject14_code = models.FileField("Subject Fourteen Code",upload_to='membership/form1_cat3/subjects', max_length=200, blank=True, null=True)
    subject15 = models.CharField("Subject Fifteen", max_length=200, blank=True, null=True)
    subject15_code = models.FileField("Subject Fifteen Code",upload_to='membership/form1_cat3/subjects', max_length=200, blank=True, null=True)

    def __str__(self):
        return 'Form One CAT3'


class Form1EndTerm(models.Model):
    subject1 = models.CharField("Subject One", max_length=200, blank=True, null=True)
    subject1_code = models.FileField("Subject One Code",upload_to='membership/form1_end_term/subjects', max_length=200, blank=True, null=True)
    subject2 = models.CharField("Subject Two", max_length=200, blank=True, null=True)
    subject2_code = models.FileField("Subject  Two Code",upload_to='membership/form1_end_term/subjects', max_length=200, blank=True, null=True)
    subject3 = models.CharField("Subject Three", max_length=200, blank=True, null=True)
    subject3_code = models.FileField("Subject Three Code",upload_to='membership/form1_end_term/subjects', max_length=200, blank=True, null=True)
    subject4 = models.CharField("Subject Four", max_length=200, blank=True, null=True)
    subject4_code = models.FileField("Subject Four Code",upload_to='membership/form1_end_term/subjects', max_length=200, blank=True, null=True)
    subject5 = models.CharField("Subject Five", max_length=200, blank=True, null=True)
    subject5_code = models.FileField("Subject Five Code",upload_to='membership/form1_end_term/subjects', max_length=200, blank=True, null=True)
    subject6 = models.CharField("Subject Six", max_length=200, blank=True, null=True)
    subject6_code = models.FileField("Subject Six Code",upload_to='membership/form1_end_term/subjects', max_length=200, blank=True, null=True)
    subject7 = models.CharField("Subject Seven", max_length=200, blank=True, null=True)
    subject7_code = models.FileField("Subject Seven Code",upload_to='membership/form1_end_term/subjects', max_length=200, blank=True, null=True)
    subject8 = models.CharField("Subject Eight", max_length=200, blank=True, null=True)
    subject8_code = models.FileField("Subject Eight Code",upload_to='membership/form1_end_term/subjects', max_length=200, blank=True, null=True)
    subject9 = models.CharField("Subject Nine", max_length=200, blank=True, null=True)
    subject9_code = models.FileField("Subject Nine Code",upload_to='membership/form1_end_term/subjects', max_length=200, blank=True, null=True)
    subject10 = models.CharField("Subject Ten", max_length=200, blank=True, null=True)
    subject10_code = models.FileField("Subject Ten Code",upload_to='membership/form1_end_term/subjects', max_length=200, blank=True, null=True)
    subject11 = models.CharField("Subject Eleven", max_length=200, blank=True, null=True)
    subject11_code = models.FileField("Subject Eleven Code",upload_to='membership/form1_end_term/subjects', max_length=200, blank=True, null=True)
    subject12 = models.CharField("Subject Twelve", max_length=200, blank=True, null=True)
    subject12_code = models.FileField("Subject Twelve Code",upload_to='membership/form1_end_term/subjects', max_length=200, blank=True, null=True)
    subject13 = models.CharField("Subject Thirteen", max_length=200, blank=True, null=True)
    subject13_code = models.FileField("Subject Thirteen Code",upload_to='membership/form1_end_term/subjects', max_length=200, blank=True, null=True)
    subject14 = models.CharField("Subject Fourteen", max_length=200, blank=True, null=True)
    subject14_code = models.FileField("Subject Fourteen Code",upload_to='membership/form1_end_term/subjects', max_length=200, blank=True, null=True)
    subject15 = models.CharField("Subject Fifteen", max_length=200, blank=True, null=True)
    subject15_code = models.FileField("Subject Fifteen Code",upload_to='membership/form1_end_term/subjects', max_length=200, blank=True, null=True)

    def __str__(self):
        return 'Form One End Term Exam'


##########################################################################################################################
# FORM TWO
# ########################################################################################################################


class Form2Cat1(models.Model):
    subject1 = models.CharField("Subject One", max_length=200, blank=True, null=True)
    subject1_code = models.FileField("Subject One Code",upload_to='membership/form2_cat1/subjects', max_length=200, blank=True, null=True)
    subject2 = models.CharField("Subject Two", max_length=200, blank=True, null=True)
    subject2_code = models.FileField("Subject  Two Code",upload_to='membership/form2_cat1/subjects', max_length=200, blank=True, null=True)
    subject3 = models.CharField("Subject Three", max_length=200, blank=True, null=True)
    subject3_code = models.FileField("Subject Three Code",upload_to='membership/form2_cat1/subjects', max_length=200, blank=True, null=True)
    subject4 = models.CharField("Subject Four", max_length=200, blank=True, null=True)
    subject4_code = models.FileField("Subject Four Code",upload_to='membership/form2_cat1/subjects', max_length=200, blank=True, null=True)
    subject5 = models.CharField("Subject Five", max_length=200, blank=True, null=True)
    subject5_code = models.FileField("Subject Five Code",upload_to='membership/form2_cat1/subjects', max_length=200, blank=True, null=True)
    subject6 = models.CharField("Subject Six", max_length=200, blank=True, null=True)
    subject6_code = models.FileField("Subject Six Code",upload_to='membership/form2_cat1/subjects', max_length=200, blank=True, null=True)
    subject7 = models.CharField("Subject Seven", max_length=200, blank=True, null=True)
    subject7_code = models.FileField("Subject Seven Code",upload_to='membership/form2_cat1/subjects', max_length=200, blank=True, null=True)
    subject8 = models.CharField("Subject Eight", max_length=200, blank=True, null=True)
    subject8_code = models.FileField("Subject Eight Code",upload_to='membership/form2_cat1/subjects', max_length=200, blank=True, null=True)
    subject9 = models.CharField("Subject Nine", max_length=200, blank=True, null=True)
    subject9_code = models.FileField("Subject Nine Code",upload_to='membership/form2_cat1/subjects', max_length=200, blank=True, null=True)
    subject10 = models.CharField("Subject Ten", max_length=200, blank=True, null=True)
    subject10_code = models.FileField("Subject Ten Code",upload_to='membership/form2_cat1/subjects', max_length=200, blank=True, null=True)
    subject11 = models.CharField("Subject Eleven", max_length=200, blank=True, null=True)
    subject11_code = models.FileField("Subject Eleven Code",upload_to='membership/form2_cat1/subjects', max_length=200, blank=True, null=True)
    subject12 = models.CharField("Subject Twelve", max_length=200, blank=True, null=True)
    subject12_code = models.FileField("Subject Twelve Code",upload_to='membership/form2_cat1/subjects', max_length=200, blank=True, null=True)
    subject13 = models.CharField("Subject Thirteen", max_length=200, blank=True, null=True)
    subject13_code = models.FileField("Subject Thirteen Code",upload_to='membership/form2_cat1/subjects', max_length=200, blank=True, null=True)
    subject14 = models.CharField("Subject Fourteen", max_length=200, blank=True, null=True)
    subject14_code = models.FileField("Subject Fourteen Code",upload_to='membership/form2_cat1/subjects', max_length=200, blank=True, null=True)
    subject15 = models.CharField("Subject Fifteen", max_length=200, blank=True, null=True)
    subject15_code = models.FileField("Subject Fifteen Code",upload_to='membership/form2_cat1/subjects', max_length=200, blank=True, null=True)

    def __str__(self):
        return 'Form Two CAT1'


class Form2Cat2(models.Model):
    subject1 = models.CharField("Subject One", max_length=200, blank=True, null=True)
    subject1_code = models.FileField("Subject One Code",upload_to='membership/form2_cat2/subjects', max_length=200, blank=True, null=True)
    subject2 = models.CharField("Subject Two", max_length=200, blank=True, null=True)
    subject2_code = models.FileField("Subject  Two Code",upload_to='membership/form2_cat2/subjects', max_length=200, blank=True, null=True)
    subject3 = models.CharField("Subject Three", max_length=200, blank=True, null=True)
    subject3_code = models.FileField("Subject Three Code",upload_to='membership/form2_cat2/subjects', max_length=200, blank=True, null=True)
    subject4 = models.CharField("Subject Four", max_length=200, blank=True, null=True)
    subject4_code = models.FileField("Subject Four Code",upload_to='membership/form2_cat2/subjects', max_length=200, blank=True, null=True)
    subject5 = models.CharField("Subject Five", max_length=200, blank=True, null=True)
    subject5_code = models.FileField("Subject Five Code",upload_to='membership/form2_cat2/subjects', max_length=200, blank=True, null=True)
    subject6 = models.CharField("Subject Six", max_length=200, blank=True, null=True)
    subject6_code = models.FileField("Subject Six Code",upload_to='membership/form2_cat2/subjects', max_length=200, blank=True, null=True)
    subject7 = models.CharField("Subject Seven", max_length=200, blank=True, null=True)
    subject7_code = models.FileField("Subject Seven Code",upload_to='membership/form2_cat2/subjects', max_length=200, blank=True, null=True)
    subject8 = models.CharField("Subject Eight", max_length=200, blank=True, null=True)
    subject8_code = models.FileField("Subject Eight Code",upload_to='membership/form2_cat2/subjects', max_length=200, blank=True, null=True)
    subject9 = models.CharField("Subject Nine", max_length=200, blank=True, null=True)
    subject9_code = models.FileField("Subject Nine Code",upload_to='membership/form2_cat2/subjects', max_length=200, blank=True, null=True)
    subject10 = models.CharField("Subject Ten", max_length=200, blank=True, null=True)
    subject10_code = models.FileField("Subject Ten Code",upload_to='membership/form2_cat2/subjects', max_length=200, blank=True, null=True)
    subject11 = models.CharField("Subject Eleven", max_length=200, blank=True, null=True)
    subject11_code = models.FileField("Subject Eleven Code",upload_to='membership/form2_cat2/subjects', max_length=200, blank=True, null=True)
    subject12 = models.CharField("Subject Twelve", max_length=200, blank=True, null=True)
    subject12_code = models.FileField("Subject Twelve Code",upload_to='membership/form2_cat2/subjects', max_length=200, blank=True, null=True)
    subject13 = models.CharField("Subject Thirteen", max_length=200, blank=True, null=True)
    subject13_code = models.FileField("Subject Thirteen Code",upload_to='membership/form2_cat2/subjects', max_length=200, blank=True, null=True)
    subject14 = models.CharField("Subject Fourteen", max_length=200, blank=True, null=True)
    subject14_code = models.FileField("Subject Fourteen Code",upload_to='membership/form2_cat2/subjects', max_length=200, blank=True, null=True)
    subject15 = models.CharField("Subject Fifteen", max_length=200, blank=True, null=True)
    subject15_code = models.FileField("Subject Fifteen Code",upload_to='membership/form2_cat2/subjects', max_length=200, blank=True, null=True)

    def __str__(self):
        return 'Form Two CAT2'


class Form2Cat3(models.Model):
    subject1 = models.CharField("Subject One", max_length=200, blank=True, null=True)
    subject1_code = models.FileField("Subject One Code",upload_to='membership/form2_cat3/subjects', max_length=200, blank=True, null=True)
    subject2 = models.CharField("Subject Two", max_length=200, blank=True, null=True)
    subject2_code = models.FileField("Subject  Two Code",upload_to='membership/form2_cat3/subjects', max_length=200, blank=True, null=True)
    subject3 = models.CharField("Subject Three", max_length=200, blank=True, null=True)
    subject3_code = models.FileField("Subject Three Code",upload_to='membership/form2_cat3/subjects', max_length=200, blank=True, null=True)
    subject4 = models.CharField("Subject Four", max_length=200, blank=True, null=True)
    subject4_code = models.FileField("Subject Four Code",upload_to='membership/form2_cat3/subjects', max_length=200, blank=True, null=True)
    subject5 = models.CharField("Subject Five", max_length=200, blank=True, null=True)
    subject5_code = models.FileField("Subject Five Code",upload_to='membership/form2_cat3/subjects', max_length=200, blank=True, null=True)
    subject6 = models.CharField("Subject Six", max_length=200, blank=True, null=True)
    subject6_code = models.FileField("Subject Six Code",upload_to='membership/form2_cat3/subjects', max_length=200, blank=True, null=True)
    subject7 = models.CharField("Subject Seven", max_length=200, blank=True, null=True)
    subject7_code = models.FileField("Subject Seven Code",upload_to='membership/form2_cat3/subjects', max_length=200, blank=True, null=True)
    subject8 = models.CharField("Subject Eight", max_length=200, blank=True, null=True)
    subject8_code = models.FileField("Subject Eight Code",upload_to='membership/form2_cat3/subjects', max_length=200, blank=True, null=True)
    subject9 = models.CharField("Subject Nine", max_length=200, blank=True, null=True)
    subject9_code = models.FileField("Subject Nine Code",upload_to='membership/form2_cat3/subjects', max_length=200, blank=True, null=True)
    subject10 = models.CharField("Subject Ten", max_length=200, blank=True, null=True)
    subject10_code = models.FileField("Subject Ten Code",upload_to='membership/form2_cat3/subjects', max_length=200, blank=True, null=True)
    subject11 = models.CharField("Subject Eleven", max_length=200, blank=True, null=True)
    subject11_code = models.FileField("Subject Eleven Code",upload_to='membership/form2_cat3/subjects', max_length=200, blank=True, null=True)
    subject12 = models.CharField("Subject Twelve", max_length=200, blank=True, null=True)
    subject12_code = models.FileField("Subject Twelve Code",upload_to='membership/form2_cat3/subjects', max_length=200, blank=True, null=True)
    subject13 = models.CharField("Subject Thirteen", max_length=200, blank=True, null=True)
    subject13_code = models.FileField("Subject Thirteen Code",upload_to='membership/form2_cat3/subjects', max_length=200, blank=True, null=True)
    subject14 = models.CharField("Subject Fourteen", max_length=200, blank=True, null=True)
    subject14_code = models.FileField("Subject Fourteen Code",upload_to='membership/form2_cat3/subjects', max_length=200, blank=True, null=True)
    subject15 = models.CharField("Subject Fifteen", max_length=200, blank=True, null=True)
    subject15_code = models.FileField("Subject Fifteen Code",upload_to='membership/form2_cat3/subjects', max_length=200, blank=True, null=True)

    def __str__(self):
        return 'Form Two CAT3'


class Form2EndTerm(models.Model):
    subject1 = models.CharField("Subject One", max_length=200, blank=True, null=True)
    subject1_code = models.FileField("Subject One Code",upload_to='membership/form2_end_term/subjects', max_length=200, blank=True, null=True)
    subject2 = models.CharField("Subject Two", max_length=200, blank=True, null=True)
    subject2_code = models.FileField("Subject  Two Code",upload_to='membership/form2_end_term/subjects', max_length=200, blank=True, null=True)
    subject3 = models.CharField("Subject Three", max_length=200, blank=True, null=True)
    subject3_code = models.FileField("Subject Three Code",upload_to='membership/form2_end_term/subjects', max_length=200, blank=True, null=True)
    subject4 = models.CharField("Subject Four", max_length=200, blank=True, null=True)
    subject4_code = models.FileField("Subject Four Code",upload_to='membership/form2_end_term/subjects', max_length=200, blank=True, null=True)
    subject5 = models.CharField("Subject Five", max_length=200, blank=True, null=True)
    subject5_code = models.FileField("Subject Five Code",upload_to='membership/form2_end_term/subjects', max_length=200, blank=True, null=True)
    subject6 = models.CharField("Subject Six", max_length=200, blank=True, null=True)
    subject6_code = models.FileField("Subject Six Code",upload_to='membership/form2_end_term/subjects', max_length=200, blank=True, null=True)
    subject7 = models.CharField("Subject Seven", max_length=200, blank=True, null=True)
    subject7_code = models.FileField("Subject Seven Code",upload_to='membership/form2_end_term/subjects', max_length=200, blank=True, null=True)
    subject8 = models.CharField("Subject Eight", max_length=200, blank=True, null=True)
    subject8_code = models.FileField("Subject Eight Code",upload_to='membership/form2_end_term/subjects', max_length=200, blank=True, null=True)
    subject9 = models.CharField("Subject Nine", max_length=200, blank=True, null=True)
    subject9_code = models.FileField("Subject Nine Code",upload_to='membership/form2_end_term/subjects', max_length=200, blank=True, null=True)
    subject10 = models.CharField("Subject Ten", max_length=200, blank=True, null=True)
    subject10_code = models.FileField("Subject Ten Code",upload_to='membership/form2_end_term/subjects', max_length=200, blank=True, null=True)
    subject11 = models.CharField("Subject Eleven", max_length=200, blank=True, null=True)
    subject11_code = models.FileField("Subject Eleven Code",upload_to='membership/form2_end_term/subjects', max_length=200, blank=True, null=True)
    subject12 = models.CharField("Subject Twelve", max_length=200, blank=True, null=True)
    subject12_code = models.FileField("Subject Twelve Code",upload_to='membership/form2_end_term/subjects', max_length=200, blank=True, null=True)
    subject13 = models.CharField("Subject Thirteen", max_length=200, blank=True, null=True)
    subject13_code = models.FileField("Subject Thirteen Code",upload_to='membership/form2_end_term/subjects', max_length=200, blank=True, null=True)
    subject14 = models.CharField("Subject Fourteen", max_length=200, blank=True, null=True)
    subject14_code = models.FileField("Subject Fourteen Code",upload_to='membership/form2_end_term/subjects', max_length=200, blank=True, null=True)
    subject15 = models.CharField("Subject Fifteen", max_length=200, blank=True, null=True)
    subject15_code = models.FileField("Subject Fifteen Code",upload_to='membership/form2_end_term/subjects', max_length=200, blank=True, null=True)

    def __str__(self):
        return 'Form Two End Term Exam'


##########################################################################################################################
# FORM THREE
# ########################################################################################################################


class Form3Cat1(models.Model):
    subject1 = models.CharField("Subject One", max_length=200, blank=True, null=True)
    subject1_code = models.FileField("Subject One Code",upload_to='membership/form3_cat1/subjects', max_length=200, blank=True, null=True)
    subject2 = models.CharField("Subject Two", max_length=200, blank=True, null=True)
    subject2_code = models.FileField("Subject  Two Code",upload_to='membership/form3_cat1/subjects', max_length=200, blank=True, null=True)
    subject3 = models.CharField("Subject Three", max_length=200, blank=True, null=True)
    subject3_code = models.FileField("Subject Three Code",upload_to='membership/form3_cat1/subjects', max_length=200, blank=True, null=True)
    subject4 = models.CharField("Subject Four", max_length=200, blank=True, null=True)
    subject4_code = models.FileField("Subject Four Code",upload_to='membership/form3_cat1/subjects', max_length=200, blank=True, null=True)
    subject5 = models.CharField("Subject Five", max_length=200, blank=True, null=True)
    subject5_code = models.FileField("Subject Five Code",upload_to='membership/form3_cat1/subjects', max_length=200, blank=True, null=True)
    subject6 = models.CharField("Subject Six", max_length=200, blank=True, null=True)
    subject6_code = models.FileField("Subject Six Code",upload_to='membership/form3_cat1/subjects', max_length=200, blank=True, null=True)
    subject7 = models.CharField("Subject Seven", max_length=200, blank=True, null=True)
    subject7_code = models.FileField("Subject Seven Code",upload_to='membership/form3_cat1/subjects', max_length=200, blank=True, null=True)
    subject8 = models.CharField("Subject Eight", max_length=200, blank=True, null=True)
    subject8_code = models.FileField("Subject Eight Code",upload_to='membership/form3_cat1/subjects', max_length=200, blank=True, null=True)
    subject9 = models.CharField("Subject Nine", max_length=200, blank=True, null=True)
    subject9_code = models.FileField("Subject Nine Code",upload_to='membership/form3_cat1/subjects', max_length=200, blank=True, null=True)
    subject10 = models.CharField("Subject Ten", max_length=200, blank=True, null=True)
    subject10_code = models.FileField("Subject Ten Code",upload_to='membership/form3_cat1/subjects', max_length=200, blank=True, null=True)
    subject11 = models.CharField("Subject Eleven", max_length=200, blank=True, null=True)
    subject11_code = models.FileField("Subject Eleven Code",upload_to='membership/form3_cat1/subjects', max_length=200, blank=True, null=True)
    subject12 = models.CharField("Subject Twelve", max_length=200, blank=True, null=True)
    subject12_code = models.FileField("Subject Twelve Code",upload_to='membership/form3_cat1/subjects', max_length=200, blank=True, null=True)
    subject13 = models.CharField("Subject Thirteen", max_length=200, blank=True, null=True)
    subject13_code = models.FileField("Subject Thirteen Code",upload_to='membership/form3_cat1/subjects', max_length=200, blank=True, null=True)
    subject14 = models.CharField("Subject Fourteen", max_length=200, blank=True, null=True)
    subject14_code = models.FileField("Subject Fourteen Code",upload_to='membership/form3_cat1/subjects', max_length=200, blank=True, null=True)
    subject15 = models.CharField("Subject Fifteen", max_length=200, blank=True, null=True)
    subject15_code = models.FileField("Subject Fifteen Code",upload_to='membership/form3_cat1/subjects', max_length=200, blank=True, null=True)

    def __str__(self):
        return 'Form Three CAT1'


class Form3Cat2(models.Model):
    subject1 = models.CharField("Subject One", max_length=200, blank=True, null=True)
    subject1_code = models.FileField("Subject One Code",upload_to='membership/form3_cat2/subjects', max_length=200, blank=True, null=True)
    subject2 = models.CharField("Subject Two", max_length=200, blank=True, null=True)
    subject2_code = models.FileField("Subject  Two Code",upload_to='membership/form3_cat2/subjects', max_length=200, blank=True, null=True)
    subject3 = models.CharField("Subject Three", max_length=200, blank=True, null=True)
    subject3_code = models.FileField("Subject Three Code",upload_to='membership/form3_cat2/subjects', max_length=200, blank=True, null=True)
    subject4 = models.CharField("Subject Four", max_length=200, blank=True, null=True)
    subject4_code = models.FileField("Subject Four Code",upload_to='membership/form3_cat2/subjects', max_length=200, blank=True, null=True)
    subject5 = models.CharField("Subject Five", max_length=200, blank=True, null=True)
    subject5_code = models.FileField("Subject Five Code",upload_to='membership/form3_cat2/subjects', max_length=200, blank=True, null=True)
    subject6 = models.CharField("Subject Six", max_length=200, blank=True, null=True)
    subject6_code = models.FileField("Subject Six Code",upload_to='membership/form3_cat2/subjects', max_length=200, blank=True, null=True)
    subject7 = models.CharField("Subject Seven", max_length=200, blank=True, null=True)
    subject7_code = models.FileField("Subject Seven Code",upload_to='membership/form3_cat2/subjects', max_length=200, blank=True, null=True)
    subject8 = models.CharField("Subject Eight", max_length=200, blank=True, null=True)
    subject8_code = models.FileField("Subject Eight Code",upload_to='membership/form3_cat2/subjects', max_length=200, blank=True, null=True)
    subject9 = models.CharField("Subject Nine", max_length=200, blank=True, null=True)
    subject9_code = models.FileField("Subject Nine Code",upload_to='membership/form3_cat2/subjects', max_length=200, blank=True, null=True)
    subject10 = models.CharField("Subject Ten", max_length=200, blank=True, null=True)
    subject10_code = models.FileField("Subject Ten Code",upload_to='membership/form3_cat2/subjects', max_length=200, blank=True, null=True)
    subject11 = models.CharField("Subject Eleven", max_length=200, blank=True, null=True)
    subject11_code = models.FileField("Subject Eleven Code",upload_to='membership/form3_cat2/subjects', max_length=200, blank=True, null=True)
    subject12 = models.CharField("Subject Twelve", max_length=200, blank=True, null=True)
    subject12_code = models.FileField("Subject Twelve Code",upload_to='membership/form3_cat2/subjects', max_length=200, blank=True, null=True)
    subject13 = models.CharField("Subject Thirteen", max_length=200, blank=True, null=True)
    subject13_code = models.FileField("Subject Thirteen Code",upload_to='membership/form3_cat2/subjects', max_length=200, blank=True, null=True)
    subject14 = models.CharField("Subject Fourteen", max_length=200, blank=True, null=True)
    subject14_code = models.FileField("Subject Fourteen Code",upload_to='membership/form3_cat2/subjects', max_length=200, blank=True, null=True)
    subject15 = models.CharField("Subject Fifteen", max_length=200, blank=True, null=True)
    subject15_code = models.FileField("Subject Fifteen Code",upload_to='membership/form3_cat2/subjects', max_length=200, blank=True, null=True)

    def __str__(self):
        return 'Form Three CAT2'


class Form3Cat3(models.Model):
    subject1 = models.CharField("Subject One", max_length=200, blank=True, null=True)
    subject1_code = models.FileField("Subject One Code",upload_to='membership/form3_cat3/subjects', max_length=200, blank=True, null=True)
    subject2 = models.CharField("Subject Two", max_length=200, blank=True, null=True)
    subject2_code = models.FileField("Subject  Two Code",upload_to='membership/form3_cat3/subjects', max_length=200, blank=True, null=True)
    subject3 = models.CharField("Subject Three", max_length=200, blank=True, null=True)
    subject3_code = models.FileField("Subject Three Code",upload_to='membership/form3_cat3/subjects', max_length=200, blank=True, null=True)
    subject4 = models.CharField("Subject Four", max_length=200, blank=True, null=True)
    subject4_code = models.FileField("Subject Four Code",upload_to='membership/form3_cat3/subjects', max_length=200, blank=True, null=True)
    subject5 = models.CharField("Subject Five", max_length=200, blank=True, null=True)
    subject5_code = models.FileField("Subject Five Code",upload_to='membership/form3_cat3/subjects', max_length=200, blank=True, null=True)
    subject6 = models.CharField("Subject Six", max_length=200, blank=True, null=True)
    subject6_code = models.FileField("Subject Six Code",upload_to='membership/form3_cat3/subjects', max_length=200, blank=True, null=True)
    subject7 = models.CharField("Subject Seven", max_length=200, blank=True, null=True)
    subject7_code = models.FileField("Subject Seven Code",upload_to='membership/form3_cat3/subjects', max_length=200, blank=True, null=True)
    subject8 = models.CharField("Subject Eight", max_length=200, blank=True, null=True)
    subject8_code = models.FileField("Subject Eight Code",upload_to='membership/form3_cat3/subjects', max_length=200, blank=True, null=True)
    subject9 = models.CharField("Subject Nine", max_length=200, blank=True, null=True)
    subject9_code = models.FileField("Subject Nine Code",upload_to='membership/form3_cat3/subjects', max_length=200, blank=True, null=True)
    subject10 = models.CharField("Subject Ten", max_length=200, blank=True, null=True)
    subject10_code = models.FileField("Subject Ten Code",upload_to='membership/form3_cat3/subjects', max_length=200, blank=True, null=True)
    subject11 = models.CharField("Subject Eleven", max_length=200, blank=True, null=True)
    subject11_code = models.FileField("Subject Eleven Code",upload_to='membership/form3_cat3/subjects', max_length=200, blank=True, null=True)
    subject12 = models.CharField("Subject Twelve", max_length=200, blank=True, null=True)
    subject12_code = models.FileField("Subject Twelve Code",upload_to='membership/form3_cat3/subjects', max_length=200, blank=True, null=True)
    subject13 = models.CharField("Subject Thirteen", max_length=200, blank=True, null=True)
    subject13_code = models.FileField("Subject Thirteen Code",upload_to='membership/form3_cat3/subjects', max_length=200, blank=True, null=True)
    subject14 = models.CharField("Subject Fourteen", max_length=200, blank=True, null=True)
    subject14_code = models.FileField("Subject Fourteen Code",upload_to='membership/form3_cat3/subjects', max_length=200, blank=True, null=True)
    subject15 = models.CharField("Subject Fifteen", max_length=200, blank=True, null=True)
    subject15_code = models.FileField("Subject Fifteen Code",upload_to='membership/form3_cat3/subjects', max_length=200, blank=True, null=True)

    def __str__(self):
        return 'Form Three CAT3'


class Form3EndTerm(models.Model):
    subject1 = models.CharField("Subject One", max_length=200, blank=True, null=True)
    subject1_code = models.FileField("Subject One Code",upload_to='membership/form3_end_term/subjects', max_length=200, blank=True, null=True)
    subject2 = models.CharField("Subject Two", max_length=200, blank=True, null=True)
    subject2_code = models.FileField("Subject  Two Code",upload_to='membership/form3_end_term/subjects', max_length=200, blank=True, null=True)
    subject3 = models.CharField("Subject Three", max_length=200, blank=True, null=True)
    subject3_code = models.FileField("Subject Three Code",upload_to='membership/form3_end_term/subjects', max_length=200, blank=True, null=True)
    subject4 = models.CharField("Subject Four", max_length=200, blank=True, null=True)
    subject4_code = models.FileField("Subject Four Code",upload_to='membership/form3_end_term/subjects', max_length=200, blank=True, null=True)
    subject5 = models.CharField("Subject Five", max_length=200, blank=True, null=True)
    subject5_code = models.FileField("Subject Five Code",upload_to='membership/form3_end_term/subjects', max_length=200, blank=True, null=True)
    subject6 = models.CharField("Subject Six", max_length=200, blank=True, null=True)
    subject6_code = models.FileField("Subject Six Code",upload_to='membership/form3_end_term/subjects', max_length=200, blank=True, null=True)
    subject7 = models.CharField("Subject Seven", max_length=200, blank=True, null=True)
    subject7_code = models.FileField("Subject Seven Code",upload_to='membership/form3_end_term/subjects', max_length=200, blank=True, null=True)
    subject8 = models.CharField("Subject Eight", max_length=200, blank=True, null=True)
    subject8_code = models.FileField("Subject Eight Code",upload_to='membership/form3_end_term/subjects', max_length=200, blank=True, null=True)
    subject9 = models.CharField("Subject Nine", max_length=200, blank=True, null=True)
    subject9_code = models.FileField("Subject Nine Code",upload_to='membership/form3_end_term/subjects', max_length=200, blank=True, null=True)
    subject10 = models.CharField("Subject Ten", max_length=200, blank=True, null=True)
    subject10_code = models.FileField("Subject Ten Code",upload_to='membership/form3_end_term/subjects', max_length=200, blank=True, null=True)
    subject11 = models.CharField("Subject Eleven", max_length=200, blank=True, null=True)
    subject11_code = models.FileField("Subject Eleven Code",upload_to='membership/form3_end_term/subjects', max_length=200, blank=True, null=True)
    subject12 = models.CharField("Subject Twelve", max_length=200, blank=True, null=True)
    subject12_code = models.FileField("Subject Twelve Code",upload_to='membership/form3_end_term/subjects', max_length=200, blank=True, null=True)
    subject13 = models.CharField("Subject Thirteen", max_length=200, blank=True, null=True)
    subject13_code = models.FileField("Subject Thirteen Code",upload_to='membership/form3_end_term/subjects', max_length=200, blank=True, null=True)
    subject14 = models.CharField("Subject Fourteen", max_length=200, blank=True, null=True)
    subject14_code = models.FileField("Subject Fourteen Code",upload_to='membership/form3_end_term/subjects', max_length=200, blank=True, null=True)
    subject15 = models.CharField("Subject Fifteen", max_length=200, blank=True, null=True)
    subject15_code = models.FileField("Subject Fifteen Code",upload_to='membership/form3_end_term/subjects', max_length=200, blank=True, null=True)

    def __str__(self):
        return 'Form Three End Term Exam'


##########################################################################################################################
# FORM FOUR
# ########################################################################################################################


class Form4Mock1(models.Model):
    subject1 = models.CharField("Subject One", max_length=200, blank=True, null=True)
    subject1_code = models.FileField("Subject One Code",upload_to='membership/form4_mock1/subjects', max_length=200, blank=True, null=True)
    subject2 = models.CharField("Subject Two", max_length=200, blank=True, null=True)
    subject2_code = models.FileField("Subject  Two Code",upload_to='membership/form4_mock1/subjects', max_length=200, blank=True, null=True)
    subject3 = models.CharField("Subject Three", max_length=200, blank=True, null=True)
    subject3_code = models.FileField("Subject Three Code",upload_to='membership/form4_mock1/subjects', max_length=200, blank=True, null=True)
    subject4 = models.CharField("Subject Four", max_length=200, blank=True, null=True)
    subject4_code = models.FileField("Subject Four Code",upload_to='membership/form4_mock1/subjects', max_length=200, blank=True, null=True)
    subject5 = models.CharField("Subject Five", max_length=200, blank=True, null=True)
    subject5_code = models.FileField("Subject Five Code",upload_to='membership/form4_mock1/subjects', max_length=200, blank=True, null=True)
    subject6 = models.CharField("Subject Six", max_length=200, blank=True, null=True)
    subject6_code = models.FileField("Subject Six Code",upload_to='membership/form4_mock1/subjects', max_length=200, blank=True, null=True)
    subject7 = models.CharField("Subject Seven", max_length=200, blank=True, null=True)
    subject7_code = models.FileField("Subject Seven Code",upload_to='membership/form4_mock1/subjects', max_length=200, blank=True, null=True)
    subject8 = models.CharField("Subject Eight", max_length=200, blank=True, null=True)
    subject8_code = models.FileField("Subject Eight Code",upload_to='membership/form4_mock1/subjects', max_length=200, blank=True, null=True)
    subject9 = models.CharField("Subject Nine", max_length=200, blank=True, null=True)
    subject9_code = models.FileField("Subject Nine Code",upload_to='membership/form4_mock1/subjects', max_length=200, blank=True, null=True)
    subject10 = models.CharField("Subject Ten", max_length=200, blank=True, null=True)
    subject10_code = models.FileField("Subject Ten Code",upload_to='membership/form4_mock1/subjects', max_length=200, blank=True, null=True)
    subject11 = models.CharField("Subject Eleven", max_length=200, blank=True, null=True)
    subject11_code = models.FileField("Subject Eleven Code",upload_to='membership/form4_mock1/subjects', max_length=200, blank=True, null=True)
    subject12 = models.CharField("Subject Twelve", max_length=200, blank=True, null=True)
    subject12_code = models.FileField("Subject Twelve Code",upload_to='membership/form4_mock1/subjects', max_length=200, blank=True, null=True)
    subject13 = models.CharField("Subject Thirteen", max_length=200, blank=True, null=True)
    subject13_code = models.FileField("Subject Thirteen Code",upload_to='membership/form4_mock1/subjects', max_length=200, blank=True, null=True)
    subject14 = models.CharField("Subject Fourteen", max_length=200, blank=True, null=True)
    subject14_code = models.FileField("Subject Fourteen Code",upload_to='membership/form4_mock1/subjects', max_length=200, blank=True, null=True)
    subject15 = models.CharField("Subject Fifteen", max_length=200, blank=True, null=True)
    subject15_code = models.FileField("Subject Fifteen Code",upload_to='membership/form4_mock1/subjects', max_length=200, blank=True, null=True)

    def __str__(self):
        return 'Form Four Mock1'


class Form4Mock2(models.Model):
    subject1 = models.CharField("Subject One", max_length=200, blank=True, null=True)
    subject1_code = models.FileField("Subject One Code",upload_to='membership/form4_mock2/subjects', max_length=200, blank=True, null=True)
    subject2 = models.CharField("Subject Two", max_length=200, blank=True, null=True)
    subject2_code = models.FileField("Subject  Two Code",upload_to='membership/form4_mock2/subjects', max_length=200, blank=True, null=True)
    subject3 = models.CharField("Subject Three", max_length=200, blank=True, null=True)
    subject3_code = models.FileField("Subject Three Code",upload_to='membership/form4_mock2/subjects', max_length=200, blank=True, null=True)
    subject4 = models.CharField("Subject Four", max_length=200, blank=True, null=True)
    subject4_code = models.FileField("Subject Four Code",upload_to='membership/form4_mock2/subjects', max_length=200, blank=True, null=True)
    subject5 = models.CharField("Subject Five", max_length=200, blank=True, null=True)
    subject5_code = models.FileField("Subject Five Code",upload_to='membership/form4_mock2/subjects', max_length=200, blank=True, null=True)
    subject6 = models.CharField("Subject Six", max_length=200, blank=True, null=True)
    subject6_code = models.FileField("Subject Six Code",upload_to='membership/form4_mock2/subjects', max_length=200, blank=True, null=True)
    subject7 = models.CharField("Subject Seven", max_length=200, blank=True, null=True)
    subject7_code = models.FileField("Subject Seven Code",upload_to='membership/form4_mock2/subjects', max_length=200, blank=True, null=True)
    subject8 = models.CharField("Subject Eight", max_length=200, blank=True, null=True)
    subject8_code = models.FileField("Subject Eight Code",upload_to='membership/form4_mock2/subjects', max_length=200, blank=True, null=True)
    subject9 = models.CharField("Subject Nine", max_length=200, blank=True, null=True)
    subject9_code = models.FileField("Subject Nine Code",upload_to='membership/form4_mock2/subjects', max_length=200, blank=True, null=True)
    subject10 = models.CharField("Subject Ten", max_length=200, blank=True, null=True)
    subject10_code = models.FileField("Subject Ten Code",upload_to='membership/form4_mock2/subjects', max_length=200, blank=True, null=True)
    subject11 = models.CharField("Subject Eleven", max_length=200, blank=True, null=True)
    subject11_code = models.FileField("Subject Eleven Code",upload_to='membership/form4_mock2/subjects', max_length=200, blank=True, null=True)
    subject12 = models.CharField("Subject Twelve", max_length=200, blank=True, null=True)
    subject12_code = models.FileField("Subject Twelve Code",upload_to='membership/form4_mock2/subjects', max_length=200, blank=True, null=True)
    subject13 = models.CharField("Subject Thirteen", max_length=200, blank=True, null=True)
    subject13_code = models.FileField("Subject Thirteen Code",upload_to='membership/form4_mock2/subjects', max_length=200, blank=True, null=True)
    subject14 = models.CharField("Subject Fourteen", max_length=200, blank=True, null=True)
    subject14_code = models.FileField("Subject Fourteen Code",upload_to='membership/form4_mock2/subjects', max_length=200, blank=True, null=True)
    subject15 = models.CharField("Subject Fifteen", max_length=200, blank=True, null=True)
    subject15_code = models.FileField("Subject Fifteen Code",upload_to='membership/form4_mock2/subjects', max_length=200, blank=True, null=True)

    def __str__(self):
        return 'Form Four Mock2'


class Form4Mock3(models.Model):
    subject1 = models.CharField("Subject One", max_length=200, blank=True, null=True)
    subject1_code = models.FileField("Subject One Code",upload_to='membership/form4_mock3/subjects', max_length=200, blank=True, null=True)
    subject2 = models.CharField("Subject Two", max_length=200, blank=True, null=True)
    subject2_code = models.FileField("Subject  Two Code",upload_to='membership/form4_mock3/subjects', max_length=200, blank=True, null=True)
    subject3 = models.CharField("Subject Three", max_length=200, blank=True, null=True)
    subject3_code = models.FileField("Subject Three Code",upload_to='membership/form4_mock3/subjects', max_length=200, blank=True, null=True)
    subject4 = models.CharField("Subject Four", max_length=200, blank=True, null=True)
    subject4_code = models.FileField("Subject Four Code",upload_to='membership/form4_mock3/subjects', max_length=200, blank=True, null=True)
    subject5 = models.CharField("Subject Five", max_length=200, blank=True, null=True)
    subject5_code = models.FileField("Subject Five Code",upload_to='membership/form4_mock3/subjects', max_length=200, blank=True, null=True)
    subject6 = models.CharField("Subject Six", max_length=200, blank=True, null=True)
    subject6_code = models.FileField("Subject Six Code",upload_to='membership/form4_mock3/subjects', max_length=200, blank=True, null=True)
    subject7 = models.CharField("Subject Seven", max_length=200, blank=True, null=True)
    subject7_code = models.FileField("Subject Seven Code",upload_to='membership/form4_mock3/subjects', max_length=200, blank=True, null=True)
    subject8 = models.CharField("Subject Eight", max_length=200, blank=True, null=True)
    subject8_code = models.FileField("Subject Eight Code",upload_to='membership/form4_mock3/subjects', max_length=200, blank=True, null=True)
    subject9 = models.CharField("Subject Nine", max_length=200, blank=True, null=True)
    subject9_code = models.FileField("Subject Nine Code",upload_to='membership/form4_mock3/subjects', max_length=200, blank=True, null=True)
    subject10 = models.CharField("Subject Ten", max_length=200, blank=True, null=True)
    subject10_code = models.FileField("Subject Ten Code",upload_to='membership/form4_mock3/subjects', max_length=200, blank=True, null=True)
    subject11 = models.CharField("Subject Eleven", max_length=200, blank=True, null=True)
    subject11_code = models.FileField("Subject Eleven Code",upload_to='membership/form4_mock3/subjects', max_length=200, blank=True, null=True)
    subject12 = models.CharField("Subject Twelve", max_length=200, blank=True, null=True)
    subject12_code = models.FileField("Subject Twelve Code",upload_to='membership/form4_mock3/subjects', max_length=200, blank=True, null=True)
    subject13 = models.CharField("Subject Thirteen", max_length=200, blank=True, null=True)
    subject13_code = models.FileField("Subject Thirteen Code",upload_to='membership/form4_mock3/subjects', max_length=200, blank=True, null=True)
    subject14 = models.CharField("Subject Fourteen", max_length=200, blank=True, null=True)
    subject14_code = models.FileField("Subject Fourteen Code",upload_to='membership/form4_mock3/subjects', max_length=200, blank=True, null=True)
    subject15 = models.CharField("Subject Fifteen", max_length=200, blank=True, null=True)
    subject15_code = models.FileField("Subject Fifteen Code",upload_to='membership/form4_mock3/subjects', max_length=200, blank=True, null=True)

    def __str__(self):
        return 'Form Four Mock3'


##########################################################################################################################
# FORM REVISION
# ########################################################################################################################


class Form4Revision(models.Model):
    subject1 = models.CharField("Subject One", max_length=200, blank=True, null=True)
    subject1_code = models.FileField("Subject One Code",upload_to='membership/form4_revision/subjects', max_length=200, blank=True, null=True)
    subject2 = models.CharField("Subject Two", max_length=200, blank=True, null=True)
    subject2_code = models.FileField("Subject  Two Code",upload_to='membership/form4_revision/subjects', max_length=200, blank=True, null=True)
    subject3 = models.CharField("Subject Three", max_length=200, blank=True, null=True)
    subject3_code = models.FileField("Subject Three Code",upload_to='membership/form4_revision/subjects', max_length=200, blank=True, null=True)
    subject4 = models.CharField("Subject Four", max_length=200, blank=True, null=True)
    subject4_code = models.FileField("Subject Four Code",upload_to='membership/form4_revision/subjects', max_length=200, blank=True, null=True)
    subject5 = models.CharField("Subject Five", max_length=200, blank=True, null=True)
    subject5_code = models.FileField("Subject Five Code",upload_to='membership/form4_revision/subjects', max_length=200, blank=True, null=True)
    subject6 = models.CharField("Subject Six", max_length=200, blank=True, null=True)
    subject6_code = models.FileField("Subject Six Code",upload_to='membership/form4_revision/subjects', max_length=200, blank=True, null=True)
    subject7 = models.CharField("Subject Seven", max_length=200, blank=True, null=True)
    subject7_code = models.FileField("Subject Seven Code",upload_to='membership/form4_revision/subjects', max_length=200, blank=True, null=True)
    subject8 = models.CharField("Subject Eight", max_length=200, blank=True, null=True)
    subject8_code = models.FileField("Subject Eight Code",upload_to='membership/form4_revision/subjects', max_length=200, blank=True, null=True)
    subject9 = models.CharField("Subject Nine", max_length=200, blank=True, null=True)
    subject9_code = models.FileField("Subject Nine Code",upload_to='membership/form4_revision/subjects', max_length=200, blank=True, null=True)
    subject10 = models.CharField("Subject Ten", max_length=200, blank=True, null=True)
    subject10_code = models.FileField("Subject Ten Code",upload_to='membership/form4_revision/subjects', max_length=200, blank=True, null=True)
    subject11 = models.CharField("Subject Eleven", max_length=200, blank=True, null=True)
    subject11_code = models.FileField("Subject Eleven Code",upload_to='membership/form4_revision/subjects', max_length=200, blank=True, null=True)
    subject12 = models.CharField("Subject Twelve", max_length=200, blank=True, null=True)
    subject12_code = models.FileField("Subject Twelve Code",upload_to='membership/form4_revision/subjects', max_length=200, blank=True, null=True)
    subject13 = models.CharField("Subject Thirteen", max_length=200, blank=True, null=True)
    subject13_code = models.FileField("Subject Thirteen Code",upload_to='membership/form4_revision/subjects', max_length=200, blank=True, null=True)
    subject14 = models.CharField("Subject Fourteen", max_length=200, blank=True, null=True)
    subject14_code = models.FileField("Subject Fourteen Code",upload_to='membership/form4_revision/subjects', max_length=200, blank=True, null=True)
    subject15 = models.CharField("Subject Fifteen", max_length=200, blank=True, null=True)
    subject15_code = models.FileField("Subject Fifteen Code",upload_to='membership/form4_revision/subjects', max_length=200, blank=True, null=True)

    def __str__(self):
        return 'Form Four Revision'
