from django.db import models
import architect

@architect.install('partition', type='range', subtype='integer', constraint='10', column='id')
class NewsArticle(models.Model):

    """ news article class to store informations in the database """

    title = models.TextField(unique=True, verbose_name="Title")
    author = models.CharField(null=True, max_length=100, blank=True, verbose_name="Author")
    description = models.TextField(null=True,blank=True, verbose_name="Description")
    content = models.TextField(null=True,blank=True, verbose_name="Content")
    url = models.URLField(max_length=3000)
    url_to_image = models.URLField(max_length=3000, null=True, blank=True) 
    published_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50, verbose_name="Category")
    country = models.CharField(blank=True,max_length=50, verbose_name="Country")
    source = models.CharField(null=True, blank=True, max_length=100, verbose_name="Source")


    class Meta:
        verbose_name_plural = "News"
    def __str__(self):
        return self.title