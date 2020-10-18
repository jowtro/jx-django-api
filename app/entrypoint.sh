#!/bin/sh

if [ "$DATABASE" = "zappit" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done
    echo "##########################"
    echo "  PostgreSQL has started  "
    echo "##########################"
fi

python manage.py flush --no-input
python manage.py migrate

exec "$@"