from rest_framework.views import APIView
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from newsapi import NewsApiClient




@api_view(['POST'])
def FetchNews(request):

