from rest_framework.decorators import api_view
from rest_framework.response import Response
from news_app.models import NewsArticle
from rest_framework import status
from django.core.cache import cache
from news_app.serializers import NewsSerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter 

import logging

logger = logging.getLogger(__name__)


@extend_schema(responses=NewsSerializer,
               description='''Endpoint to get all News articles.''')
@api_view(['GET'])
def get_all_news(request):
    try:
        # Attempt to retrieve cached data
        cached_data = cache.get('all_news')
        # check if data is in the cache
        if cached_data:
            return Response({'success': cached_data}, status=status.HTTP_200_OK)
        
        # If data is not cached, fetch it from the database
        news = NewsArticle.objects.all()
        if news:
            serializer = NewsSerializer(news, many=True)
            result = serializer.data
            # Cache the fetched data
            cache.set('all_news', result, timeout=3600) # Cache for 1 hour 
            return Response({'success': result}, status=status.HTTP_200_OK)
        else:
            return Response({'success': 'There are no articles available at the moment'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': f'Failed to retrieve news articles. {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#################################################
############### Get data by Category ###########
#################################################
@extend_schema(responses=NewsSerializer,
               parameters=[
        OpenApiParameter(name='category', description='<description>', 
                         required=True, type=str),
    ],
    description='''Endpoint to get News by category \n 
                    example : business, entertainment, health, science, sports, technology ''')
@api_view(['GET'])
def get_news_by_category(request):
    try:
        categories = ['business', 'entertainment', 'health', 'science', 'sports', 'technology']
        category = request.query_params.get('category')  
        if category not in categories:
            return Response({'error': f'The category {category} does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Attempt to retrieve cached data
        cached_data = cache.get(f'news_by_category_{category}')
        # check if data in the cache
        if cached_data:
            return Response({'success': cached_data}, status=status.HTTP_200_OK)
        
        # If data is not cached, fetch it from the database
        news = NewsArticle.objects.filter(category=category)
        if news:
            serializer = NewsSerializer(news, many=True)
            result = serializer.data
            # Cache the fetched data
            cache.set(f'news_by_category_{category}', result, timeout=3600) # Cache for 1 hour 
            return Response({'success': result}, status=status.HTTP_200_OK)
        else:
            return Response({'success': 'There is no articles in this category at the moment'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': f'Category retrieval failed. {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#################################################
############### Get data by Country #############
#################################################
@extend_schema(responses=NewsSerializer,
               parameters=[
        OpenApiParameter(name='country', description='<description>', 
                         required=True, type=str),
    ],
    description=''' Endpoint to get News by country \n  
                    example : us , ae , gb ''')
@api_view(['GET'])
def get_news_by_country(request):
    try:
        countries = ['us', 'ae', 'gb']
        country = request.query_params.get('country')  
        if country not in countries:
            return Response({'error': f'The country {country} does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Attempt to retrieve cached data
        cached_data = cache.get(f'news_by_country_{country}')
        # check if data in the cache
        if cached_data:
            return Response({'success': cached_data}, status=status.HTTP_200_OK)
        
        # If data is not cached, fetch it from the database
        news = NewsArticle.objects.filter(country=country)
        if news:
            serializer = NewsSerializer(news, many=True)
            result = serializer.data
            # Cache the fetched data
            cache.set(f'news_by_country_{country}', result, timeout=3600) # Cache for 1 hour 
            return Response({'success': result}, status=status.HTTP_200_OK)
        else:
            return Response({'success': 'There is no articles for this country at the moment'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': f'country retrieval failed. {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#################################################
############### Get data by Source #############
#################################################
@extend_schema(responses=NewsSerializer,
               parameters=[
        OpenApiParameter(name='source', description='<description>', 
                         required=True, type=str),
    ],
    description=''' Endpoint to get News by source \n  
                    example : MacRumors, IGN, CNET, CNN, The Wall Street Journal, YouTube ,ESPN, BBC News, Google News ,CBS News ,The Hill, MSNBC , RTL Nieuws , TechCrunch ,Fox News , Bloomberg, TechCrunch, Al Jazeera English ''')
@api_view(['GET'])
def get_news_by_source(request):
    try:
        sources = ['MacRumors', 'IGN', 'CNET','CNN', 'The Wall Street Journal','YouTube', 'ESPN', 'BBC News','Google News', 'CBS News','The Hill', 'MSNBC', 'RTL Nieuws', 'TechCrunch' , 'Fox News' , 'Bloomberg', 'TechCrunch', 'Al Jazeera English' ]
        source = request.query_params.get('source')  
        if source not in sources:
            return Response({'error': f'The source {source} does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Attempt to retrieve cached data
        cached_data = cache.get(f'news_by_source_{source}')
        # check if data in the cache
        if cached_data:
            return Response({'success': cached_data}, status=status.HTTP_200_OK)
        
        # If data is not cached, fetch it from the database
        news = NewsArticle.objects.filter(source=source)
        if news:
            serializer = NewsSerializer(news, many=True)
            result = serializer.data
            # Cache the fetched data
            cache.set(f'news_by_source_{source}', result, timeout=3600) # Cache for 1 hour 
            return Response({'success': result}, status=status.HTTP_200_OK)
        else:
            return Response({'success': 'There is no articles for this source at the moment'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': f'source retrieval failed. {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

