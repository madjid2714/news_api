from news_app.tasks import update_news_data


update_news_data.delay()
