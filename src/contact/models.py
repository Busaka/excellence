from django.db import models

# Create your models here.


class Contact(models.Model):

    """Docstring for Contact. """
    subject = models.CharField(max_length=1000)
    email = models.EmailField()
    message = models.TextField()
