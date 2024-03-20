from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.http import JsonResponse
from rest_framework.response import Response
from news_app.models import NewsArticle
from rest_framework import status

@api_view(['GET'])
def get_news_by_category(request, category):
    try:
        news = NewsArticle.objects.filter(category=category)

        # Serialize the queryset to JSON
        news_data = [{'title': article.title,
                    'description': article.description,
                    'author': article.description,
                    'content': article.content,
                    'published_at': article.published_at,
                    'source': article.source,
                    'url': article.url,
                    'url_to_image': article.url_to_image,
                    'category': article.category,
                    'country': article.country,
                    } for article in news]
        return Response({'success': news_data }, status=status.HTTP_200_OK)
    except news.DoesNotExist:
        return Response({'error': f'The category {category}: does not exist '}, status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response({'error': f' Category recupuration failed. {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# def get_news_by_country(request, country):
#     news = NewsArticle.objects.filter(country=country)
#     # Serialize the queryset to JSON
#     news_data = [{'title': article.title, 'content': article.content} for article in news]
#     return JsonResponse({'news': news_data})

# Define more API endpoints for source, query, etc.

# @api_view(['GET'])
# # def FetchNews(request):
# def FetchNews(request):
#     newsapi = NewsApiClient(api_key=settings.NEWS_API_KEY)
#     news_data = newsapi.get_top_headlines(
#         country='us',
#         # category='technology',
#     )
#     return Response({'news': news_data})

