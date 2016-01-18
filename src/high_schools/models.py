from django.db import models

# Create your models here.


class HighSchool(models.Model):
    """Docstring for Schools. """
    featured = models.CharField(max_length=200)
    high_school_name = models.CharField(max_length=200)
    high_school_logo = models.ImageField(upload_to='school_photos', blank=True)

    high_school_motto = models.CharField(max_length=200)

    high_school_photo1 = models.ImageField(upload_to='school_photos', blank=True)
    description1 = models.TextField(blank=True)

    high_school_photo2 = models.ImageField(upload_to='school_photos', blank=True)
    description2 = models.TextField(blank=True)
    
    high_school_photo3 = models.ImageField(upload_to='school_photos', blank=True)
    description3 = models.TextField(blank=True)
    
    high_school_photo4 = models.ImageField(upload_to='school_photos', blank=True)
    description4 = models.TextField(blank=True)
    
    high_school_photo5 = models.ImageField(upload_to='school_photos', blank=True)
    description5 = models.TextField(blank=True)
    
    published = models.DateTimeField(auto_now_add=True, auto_now=False)

    # address
    po_box = models.CharField(max_length=20)
    location = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    website = models.CharField(max_length=100, blank=True)

    # special coursesnoffered
    suject_one = models.CharField(max_length=200, blank=True)
    suject_two = models.CharField(max_length=200, blank=True)
    suject_three = models.CharField(max_length=200, blank=True)
    suject_four = models.CharField(max_length=200, blank=True)
    suject_five = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.high_school_name

