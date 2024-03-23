# news_api
Latest News Dashboard using Django, Django REST, Postgresql and Angular with Database Optimization
# Description
a web application with Django and Django REST framework as the backend to fetch
news from the News API, incorporating database optimizations, and display it on a front-end
built with Angular.
# structure
```
news_web_app/
|-- news_backend/         # Django Backend
|   |-- news_app/         # Django App
|   |   |-- api/          # Rest API
|   |   |  |-- __init__.py
|   |   |  |-- urls.py
|   |   |  |-- views.py
|   |   |-- migrations/
|   |   |-- __init__.py
|   |   |-- admin.py
|   |   |-- apps.py
|   |   |-- models.py
|   |   |-- serializers.py
|   |   |-- tasks.py      #  Celery task that fetches news data from the News API and updates your Django model
|   |   |-- urls.py
|   |   |-- views.py
|   |-- news_web_app/     # Django Project
|   |   |-- __init__.py
|   |   |-- celery.py     # celery configuraion
|   |   |-- settings.py
|   |   |-- urls.py
|   |   |-- wsgi.py
|-- frontend/             # Angular Frontend not implemented yet
|-- manage.py
```
# Setup
Clone project
```shell
$ git@github.com:madjid2714/django_blog.git
```
```shell
$ cd django_blog
```
install redis 
```shell
sudo apt instal redis
```
Install requirement
```shell
$ pip install -r requirement.txt
```
enter to postgres:
```shell
$ sudo -u postgres psql
```
create datbase:
```sql
CREATE DATABASE newsdb;
```
cretae user with password:
```sql
CREATE USER admin WITH PASSWORD 'dbpassword';
```
setting the default encoding to utf-8 and time zone to utc, and default_transactions to read commited:

```sql
ALTER ROLE admin SET client_encoding TO 'utf8';
ALTER ROLE admin SET default_transaction_isolation TO 'read committed';
ALTER ROLE admin SET timezone TO 'UTC';
```
COnfigure database in django settings.py
```python
# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'newsdb',
        'USER': 'admin',
        'PASSWORD':'dbpassword',
        'HOST': 'localhost',
        'PORT':'5432',
    }
}
```
migrate databse :
```shell
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```
create superuser:
```shell
$ python3 manage.py createsuperuser
```
Create the partitions using the command:
```shell
$export DJANGO_SETTINGS_MODULE=news_backend.settings
$ architect partition --module news_app.models
architect partition: result: successfully (re)configured the database for the following models: NewsArticle 
```
start the celery worker :
```shell
$ celery -A news_backend worker --loglevel=info
$ celery -A news_backend beat --loglevel=info
```
run server and test the app:
```shell
$ python3 manage.py runserver
```
now you can acces to http://localhost:8000/admin/  to see the news

# Eendpoints
country_retrieve example : http://localhost:8000/api/category/?country=us
category_retrieve example : http://localhost:8000/api/category/?category=technology
source_retrieve example : http://localhost:8000/api/source/?source=IGN

