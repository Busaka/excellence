from django.db import models


# Create your models here.


class College(models.Model):
    """Docstring for Contact. """
    featured = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    college_logo = models.ImageField(upload_to='colleges/college_photos') 
    college_motto = models.CharField(max_length=500)

    photo1 = models.ImageField(upload_to='colleges/college_photos') 
    description1 = models.TextField(blank=True)
    college_photo2 = models.ImageField(upload_to='colleges/college_photos') 
    description2 = models.TextField(blank=True)
    college_photo3 = models.ImageField(upload_to='colleges/college_photos') 
    description3 = models.TextField(blank=True)
    college_photo4 = models.ImageField(upload_to='colleges/college_photos') 
    description4 = models.TextField(blank=True)
    college_photo5 = models.ImageField(upload_to='colleges/college_photos') 
    description5 = models.TextField(blank=True)

    published = models.DateTimeField(auto_now_add=True, auto_now=False)

    po_box = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    email = models.EmailField()
    website = models.CharField(max_length=500, blank=True)

    course_one = models.CharField(max_length=500, blank=True)
    course_two = models.CharField(max_length=500, blank=True)
    course_three = models.CharField(max_length=500, blank=True)
    course_four = models.CharField(max_length=500, blank=True)
    course_five = models.CharField(max_length=500, blank=True)
    college_file = models.FileField(upload_to='colleges/college_files', blank=True)

    def __str__(self):
        return self.college_name

