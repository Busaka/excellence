from django.db import models

# Create your models here.


class Article(models.Model):
    heading_one = models.CharField(max_length=500)
    question = models.TextField()
    answer = models.TextField()
    image_one = models.ImageField() 

    heading_two = models.CharField(max_length=500)
    text_two = models.TextField()
    image_two = models.ImageField() 

    heading_three = models.CharField(max_length=500)
    text_three = models.TextField()
    image_three = models.ImageField() 

    heading_four = models.CharField(max_length=500)
    text_four = models.TextField()
    image_four = models.ImageField() 

    heading_five = models.CharField(max_length=500)
    text_five = models.TextField()
    image_five = models.ImageField() 

    heading_six = models.CharField(max_length=500)
    text_six = models.TextField()
    image_six = models.ImageField() 

    pub_date = models.DateTimeField('Date Published', auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.pub_date)
