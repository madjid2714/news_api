# News app
News web api using Django, Django REST, Postgresql and Angular with Database Optimization.
# Description
a web application with Django and Django REST framework as the backend to fetch
news from the News API, incorporating database optimizations.

- The following architecture shows the components:
<img src="https://github.com/madjid2714/news_api/blob/main/Dark_news_api.png">

# Structure
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
|   |   |-- tasks.py   #  Celery task that fetches news data from the News API and updates Django model
|   |   |-- urls.py
|   |   |-- views.py
|   |-- news_web_app/     # Django Project
|   |   |-- __init__.py
|   |   |-- celery.py     # Celery configuraion
|   |   |-- settings.py
|   |   |-- urls.py
|   |   |-- wsgi.py
|-- frontend/             # Angular Frontend not implemented yet
|-- .env        # To store NEWS_API_KEY and environemen vribales
|-- manage.py
|-- schema.yml   # The genrated schema for Api documentation
```
# Docker Setup (Optional) ![alt text](https://camo.githubusercontent.com/fc8c91a1c1a2e8b4b0bf5f4ddbaec59d1f1159770294459ad8263b077fafb1bc/68747470733a2f2f736b696c6c69636f6e732e6465762f69636f6e733f693d646f636b6572)
If you want to use Docker to run this project, you need to do the following steps:<br>

- Clone project
```shell
$ https://github.com/madjid2714/news_api.git
```
```shell
$ cd news_api
```
- First, you need to modify the **.env** file and add the **NEWS_API_KEY**, **PostgreSQL** credentials, and the initial **Django superuser**:

```env
# example
NEWS_API_KEY = 'Your news API goes here bring it from newsapi.org'

# PostgreSQL credentials
POSTGRES_DB=your_db_name 
POSTGRES_USER=your_db_user
POSTGRES_PASSWORD=your_db_password
POSTGRES_HOST=your_db_host

# Django superuser credentials
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=adminpassword
```
- Run ``docker compose build``
- Run ``docker compose up``
- Endpoints <br>
    List all news example : http://localhost:8000/api/all <br>
    country_retrieve  : http://localhost:8000/api/category/?country=us <br>
    category_retrieve  : http://localhost:8000/api/category/?category=technology <br>
    source_retrieve  : http://localhost:8000/api/source/?source=IGN <br>

- API documentation: <br>
    Swagger ui : http://localhost:8000/api/docs <br>
    Redoc ui : http://localhost:8000/api/redoc 

To stop the container, run ``docker compose stop`` <br>
To restart the container, run ``docker compose start`` <br>
To delete the container, run ``docker compose down`` <br>


# Setup (in host machine)
Clone project
```shell
$ https://github.com/madjid2714/news_api.git
```
```shell
$ cd news_api
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
Configure database in django settings.py
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
$ export DJANGO_SETTINGS_MODULE=news_backend.settings
$ architect partition --module news_app.models
architect partition: result: successfully (re)configured the database for the following models: NewsArticle 
```
start the celery worker :
```shell
$ celery -A news_backend worker --loglevel=info
$ celery -A news_backend beat --loglevel=info
```

Generate schema.yml  for API documentation :
```shell
$ python manage.py  spectacular --color --file schema.yml
```
Go the newsapi.org/ and get NEWS_API_KEY and put the key in the .env file :
```env
# example
NEWS_API_KEY = 'Your news API goes here bring it from newsapi.org'
```
run server and test the app:
```shell
$ python3 manage.py runserver
```

# Endpoints
List all news example : http://localhost:8000/api/all <br>
country_retrieve  : http://localhost:8000/api/category/?country=us <br>
category_retrieve  : http://localhost:8000/api/category/?category=technology <br>
source_retrieve  : http://localhost:8000/api/source/?source=IGN <br>

# API documentation:
Swagger ui : http://localhost:8000/api/docs <br>
Redoc ui : http://localhost:8000/api/redoc <br>

