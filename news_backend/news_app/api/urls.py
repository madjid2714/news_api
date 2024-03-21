from django.urls import path, include
from news_app.api import views

urlpatterns = [
 path('category/', views.get_news_by_category, name='get_news_by_category'),
]