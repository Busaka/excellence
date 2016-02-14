from django.db import models

# Create your models here.


class HighSchool(models.Model):
    featured = models.CharField(max_length=500)
    high_school_name = models.CharField(max_length=500)
    high_school_logo = models.ImageField(upload_to='high_school/high_school_photos') 
    high_school_motto = models.CharField(max_length=500)

    high_school_photo1 = models.ImageField(upload_to='high_school/high_school_photos') 
    description1 = models.TextField(blank=True)
    high_school_photo2 = models.ImageField(upload_to='high_school/high_school_photos') 
    description2 = models.TextField(blank=True)
    high_school_photo3 = models.ImageField(upload_to='high_school/high_school_photos') 
    description3 = models.TextField(blank=True)
    high_school_photo4 = models.ImageField(upload_to='high_school/high_school_photos') 
    description4 = models.TextField(blank=True)
    high_school_photo5 = models.ImageField(upload_to='high_school/high_school_photos') 
    description5 = models.TextField(blank=True)

    published = models.DateTimeField(auto_now_add=True, auto_now=False)

    po_box = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    email = models.EmailField()
    website = models.CharField(max_length=500, blank=True)

    # special courses
    course_one = models.CharField(max_length=500, blank=True)
    course1_link = models.CharField(max_length=500, blank=True)
    course_two = models.CharField(max_length=500, blank=True)
    course2_link = models.CharField(max_length=500, blank=True)
    course_three = models.CharField(max_length=500, blank=True)
    course3_link = models.CharField(max_length=500, blank=True)
    course_four = models.CharField(max_length=500, blank=True)
    course4_link = models.CharField(max_length=500, blank=True)
    course_five = models.CharField(max_length=500, blank=True)
    course5_link = models.CharField(max_length=500, blank=True)

    high_school_file = models.FileField(upload_to='high_school/high_school_files', blank=True)

    # social networks
    facebook = models.CharField(max_length=500, blank=True)
    twitter = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.high_school_name
