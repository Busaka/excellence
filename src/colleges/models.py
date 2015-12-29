from django.db import models


# Create your models here.


class College(models.Model):
    """Docstring for Schools. """
    college_name = models.CharField(max_length=200)
    description = models.TextField()
    college_photo = models.ImageField(upload_to='school_photos')
    published = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.college_name

