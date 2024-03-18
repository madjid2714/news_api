from rest_framework import serializers
from .models import News


class NewsSerializer(serializers.Serializer):

    """ Serializer Django REST Framework for the news model"""
    class Meta:
        model = News
        fields = '__all__'
        
