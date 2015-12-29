from django.db import models


# Create your models here.


class Job(models.Model):

    """Docstring for . """
    school = models.CharField(max_length=200)
    email = models.EmailField()
    job_title = models.CharField(max_length=200)
    job_description = models.TextField()
