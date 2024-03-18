from django.db import models

# Create your models here.

class News(models.Model):

    """ news class to store informations about news post """

    title = models.CharField(max_length=255, unique=True, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    url = models.URLField(max_length = 200) 
    image = models.ImageField(blank=True, upload_to='image/')
    