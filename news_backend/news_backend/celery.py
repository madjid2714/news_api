# from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_backend.settings')

# app = Celery('news_backend', broker="redis://localhost:6379", backend="redis://localhost:6379")
app = Celery('news_backend')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
