from django.db import models

# Create your models here.


class HighSchool(models.Model):
    """Docstring for Schools. """
    high_school_name = models.CharField(max_length=200)
    description = models.TextField()
    high_school_photo = models.ImageField(upload_to='school_photos')
    published = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.high_school_name

