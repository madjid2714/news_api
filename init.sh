#!/bin/bash

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."
    sleep 0.3
    echo "PostgreSQL started"
fi
set -e

>&2 echo "Postgres is up - continuing"
# Check if initialization tasks have been performed
if [ ! -f /usr/src/app/initialized ]; then
    # Perform initialization tasks (database migrations)
    python manage.py flush --no-input
    python manage.py makemigrations && python manage.py makemigrations news_app
    python manage.py migrate
    # python manage.py migrate && createsuperuser2 --username# test1 --password 123456 --noinput --email 'blank@email.com
    python manage.py createsuperuser --noinput;\
    python manage.py  spectacular --color --file schema.yml

    DJANGO_SETTINGS_MODULE=news_backend.settings
    architect partition --module news_app.models
    # Create a file to indicate that initialization is complete
    touch /usr/src/app/initialized
    
    python manage.py runserver 0.0.0.0:8000



else
    python manage.py runserver 0.0.0.0:8000
fi

while ! python manage.py showmigrations --plan | grep '\[ \]' >/dev/null; do
    echo "Waiting for migrations to complete..."
    sleep 1
done

exec "$@"
