from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.http import JsonResponse
from rest_framework.response import Response
from news_app.models import NewsArticle
from rest_framework import status
# from cacheops import cache
from django.core.cache import cache

from django.views.decorators.cache import cache_page

import redis

# # Connect to Redis
# redis_client = redis.Redis(host='localhost', port=6379, db=0)

# @api_view(['GET'])
# def get_news_by_category(request):
#     # Check if the data is already cached
#     cached_data = redis_client.get('cached_data')
#     if cached_data:
#         # Data found in cache, return it
#         print(f"===categ====")
#         return Response({'success': 'cache'}, status=status.HTTP_200_OK)
#     else:
#         # Simulate expensive operation to fetch data
#         expensive_data = {'example': 'This is some expensive data'}

#         # Store the data in cache for future requests
#         redis_client.setex('cached_data', 60, str(expensive_data))

#         # Data retrieved from source and inserted into cache, return it
#         return Response({'success': 'source'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def get_news_by_category(request):
    try:
        categories = ['business', 'entertainment', 'health', 'science', 'sports', 'technology']
        category = request.data.get('category')
        print(f"===categ==== {category}")
        if category not in categories:
            return Response({'error': f'The category {category} does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Attempt to retrieve cached data
        print(f"==== 1 ==== ")
        cache.set('test_key', 'test_value', timeout=60)
        print(f"==== 2 ==== ")
        print(cache.get('test_key'))
        cached_data = cache.get(f'news_by_category_technology')
        print(f"==== 3 ==== ")
        if cached_data:
            print(f"==== in cached data ==== ")
            return Response({'success': cached_data}, status=status.HTTP_200_OK)
        
        # If data is not cached, fetch it from the database
        news = NewsArticle.objects.filter(category=category)
        print(f"==== news ==== {news}")
        if news:
            news_data = [{'title': article.title,
                          'description': article.description,
                          'author': article.author,  # Assuming author field
                          'content': article.content,
                          'published_at': article.published_at,
                          'source': article.source,
                          'url': article.url,
                          'url_to_image': article.url_to_image,
                          'category': article.category,
                          'country': article.country,
                          } for article in news]
            # Cache the fetched data
            cache.set(f'news_by_category_{category}', news_data, timeout=30) # Cache for 1 hour
            return Response({'success': news_data}, status=status.HTTP_200_OK)
        else:
            return Response({'success': 'There are no articles in this category at the moment'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': f'Category retrieval failed. {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



# @api_view(['GET'])
# def get_news_by_category(request, category):
#     try:
#         categories = ['business', 'entertainment', 'health', 'science', 'sports', 'technology']
#         if category not in categories:
#             return Response({'error': f'The category {category} does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        
#         news = NewsArticle.objects.filter(category=category)

#         if news:
#             news_data = [{'title': article.title,
#                           'description': article.description,
#                           'author': article.author,                          'content': article.content,
#                           'published_at': article.published_at,
#                           'source': article.source,
#                           'url': article.url,
#                           'url_to_image': article.url_to_image,
#                           'category': article.category,
#                           'country': article.country,
#                           } for article in news]
#             return Response({'success': news_data}, status=status.HTTP_200_OK)
#         else:
#             return Response({'success': 'There are no articles in this category at the moment'}, status=status.HTTP_200_OK)
#     except Exception as e:
#         return Response({'error': f'Category retrieval failed. {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





# @api_view(['GET'])
# # def FetchNews(request):
# def FetchNews(request):
#     newsapi = NewsApiClient(api_key=settings.NEWS_API_KEY)
#     news_data = newsapi.get_top_headlines(
#         country='us',
#         # category='technology',
#     )
#     return Response({'news': news_data})

