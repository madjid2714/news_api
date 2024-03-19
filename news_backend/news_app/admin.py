from django.contrib import admin
from .models import NewsArticle
# Register your models here.


""" Show News in the django admin panel """
admin.site.register(NewsArticle)