from django.db import models

# Create your models here.


class Job(models.Model):

    """
    Docstring for Job. 
    """
    publish = models.CharField(max_length=20)
    school = models.CharField(max_length=200)
    email = models.EmailField()
    phone  = models.CharField(max_length=200, blank=True)
    website  = models.CharField(max_length=200, blank=True)
    job_title = models.CharField(max_length=200)
    job_description1 = models.TextField('Job Description')
    job_description2 = models.TextField('Paragraph Two(Optional)', blank=True)
    job_description3 = models.TextField('Paragraph Three(Optional)', blank=True)
    job_description4 = models.TextField('Paragraph Four(Optional)', blank=True)
    job_description5 = models.TextField('Paragraph Five(Optional)', blank=True)
    pub_date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.job_title

# Create your models here.
