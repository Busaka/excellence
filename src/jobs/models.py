from django.db import models


# Create your models here.


class Job(models.Model):

    """Docstring for . """
    school = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    description = models.TextField()
