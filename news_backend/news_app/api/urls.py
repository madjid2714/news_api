from django.urls import path
from news_app.api import views
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
 path('all/', views.get_all_news, name='get_all_news'),
 path('category/', views.get_news_by_category, name='get_news_by_category'),
 path('country/', views.get_news_by_country, name='get_news_by_country'),
 path('source/', views.get_news_by_source, name='get_news_by_source'),
 path('schema/', SpectacularAPIView.as_view(), name='schema'),
 path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
 path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]