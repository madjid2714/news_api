from celery import shared_task
from news_app.models import NewsArticle
from django.conf import settings
from newsapi import NewsApiClient
import logging
logger = logging.getLogger(__name__)

@shared_task
def update_news_data():
    logger.info("Updating news data...")
    categories = ['business', 'entertainment', 'health', 'science', 'sports', 'technology']
    countries = ['ae', 'us', 'gb']
    for category in categories:
        for country in countries:
            newsapi = NewsApiClient(api_key=settings.NEWS_API_KEY)
            news_data = newsapi.get_top_headlines(
                country=country,
                # page=1
                category=category
            )
            for article_data in news_data['articles']:
                NewsArticle.objects.update_or_create(
                    title = article_data["title"],
                    defaults={
                        "title": article_data["title"],
                        "description": article_data.get("description", ""),
                        "content": article_data["content"],
                        "author": article_data.get("author", ""),
                        "published_at": article_data["publishedAt"],
                        "source": article_data["source"]["name"],
                        "url": article_data["url"],
                        "url_to_image": article_data.get("urlToImage", ""),
                        "category": category,
                        "country": country,
                    }
                )

    logger.info("News data updated successfully.")
