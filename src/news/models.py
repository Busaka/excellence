from django.db import models

# Create your models here.

class New(models.Model):
    heading_one = models.CharField(max_length=500)
    text_one = models.TextField()
    image_one = models.ImageField() 
    file_one = models.FileField()

    heading_two = models.CharField(max_length=500)
    text_two = models.TextField()
    image_two = models.ImageField() 
    file_two = models.FileField()

    heading_three = models.CharField(max_length=500)
    text_three = models.TextField()
    image_three = models.ImageField() 
    file_three = models.FileField()

    heading_four = models.CharField(max_length=500)
    text_four = models.TextField()
    image_four = models.ImageField() 
    file_four = models.FileField()

    heading_five = models.CharField(max_length=500)
    text_five = models.TextField()
    image_five = models.ImageField() 
    file_five = models.FileField()
    pub_date = models.DateTimeField('Date Published', auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.pub_date)
