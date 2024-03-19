from django.db import models

# Create your models here.

class NewsArticle(models.Model):

    """ news article class to store informations in the database """

    title = models.CharField(max_length=255, unique=True, verbose_name="Title")
    author = models.CharField(max_length=100, blank=True, verbose_name="Author")
    description = models.TextField(blank=True, verbose_name="Description")
    content = models.TextField(verbose_name="Content")
    url = models.URLField(max_length=255)
    url_to_image = models.URLField(blank=True) 
    # image = models.ImageField(null=True, blank=True, upload_to='image/')

    published_at = models.DateTimeField(auto_now_add=True)
    # updatedAt = models.DateTimeField(auto_now=True)

    category = models.CharField(max_length=50, verbose_name="Category")
    country = models.CharField(max_length=50, verbose_name="Country")
    source = models.CharField(max_length=100, verbose_name="Source")


    class Meta:
        verbose_name_plural = "News"
    def __str__(self):
        return self.title