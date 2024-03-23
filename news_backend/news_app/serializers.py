from rest_framework import serializers
from .models import NewsArticle


class NewsSerializer(serializers.ModelSerializer):

    """ Serializer Django REST Framework for the news model"""

    class Meta:
        model = NewsArticle
        fields = '__all__'
        
