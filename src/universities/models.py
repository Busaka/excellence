from django.db import models

# Create your models here.


class LocalUniversities(models.Model):
    """Docstring for LocalUniversities. """
    featured = models.CharField(max_length=500)
    university_name = models.CharField(max_length=200)
    university_logo = models.ImageField(upload_to='universities/university_photos') 
    university_motto = models.CharField(max_length=500)

    university_photo1 = models.ImageField(upload_to='universities/university_photos') 
    description1 = models.TextField(blank=True)
    university_photo2 = models.ImageField(upload_to='universities/university_photos') 
    description2 = models.TextField(blank=True)
    university_photo3 = models.ImageField(upload_to='universities/university_photos') 
    description3 = models.TextField(blank=True)
    university_photo4 = models.ImageField(upload_to='universities/university_photos') 
    description4 = models.TextField(blank=True)
    university_photo5 = models.ImageField(upload_to='universities/university_photos') 
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

    def __str__(self):
        return self.university_name


class InternationalUniversities(models.Model):
    """Docstring for InternationalUniversities. """
    featured = models.CharField(max_length=500)
    university_name = models.CharField(max_length=200)
    university_logo = models.ImageField(upload_to='universities/university_photos') 
    university_motto = models.CharField(max_length=500)

    university_photo1 = models.ImageField(upload_to='universities/university_photos') 
    description1 = models.TextField(blank=True)
    university_photo2 = models.ImageField(upload_to='universities/university_photos') 
    description2 = models.TextField(blank=True)
    university_photo3 = models.ImageField(upload_to='universities/university_photos') 
    description3 = models.TextField(blank=True)
    university_photo4 = models.ImageField(upload_to='universities/university_photos') 
    description4 = models.TextField(blank=True)
    university_photo5 = models.ImageField(upload_to='universities/university_photos') 
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

    def __str__(self):
        return self.university_name

