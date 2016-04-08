from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.StudyTip)
admin.site.register(models.BasicForm1Exam)
admin.site.register(models.BasicForm2Exam)
admin.site.register(models.BasicForm3Exam)
admin.site.register(models.BasicForm4Exam)

# Premium exams
#
# Form One
admin.site.register(models.Form1Cat1)
admin.site.register(models.Form1Cat2)
admin.site.register(models.Form1Cat3)
admin.site.register(models.Form1EndTerm)

# Form Two
admin.site.register(models.Form2Cat1)
admin.site.register(models.Form2Cat2)
admin.site.register(models.Form2Cat3)
admin.site.register(models.Form2EndTerm)

# Form Three
admin.site.register(models.Form3Cat1)
admin.site.register(models.Form3Cat2)
admin.site.register(models.Form3Cat3)
admin.site.register(models.Form3EndTerm)

# Form Four
admin.site.register(models.Form4Mock1)
admin.site.register(models.Form4Mock2)
admin.site.register(models.Form4Mock3)
admin.site.register(models.Form4Revision)
