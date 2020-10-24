#!/bin/bash
set -e

echo "########################################"
echo "#      CHECK IF POSTGRESQL IS UP       #"
echo "########################################"
echo "Waiting PostgreSQL"
python check-pgsql.py
echo "finished ..."


echo "########################################"
echo "#      CHECK ENVIRONMENT VARIABLES     #"
echo "########################################"
echo "DEBUG $DEBUG"
echo "SECRET_KEY $SECRET_KEY"
echo "DJANGO_ALLOWED_HOSTS $DJANGO_ALLOWED_HOSTS"
echo "SQL_ENGINE $SQL_ENGINE"
echo "POSTGRES_DB $POSTGRES_DB"
echo "POSTGRES_USER $POSTGRES_USER"
echo "POSTGRES_PASSWORD $POSTGRES_PASSWORD"
echo "SQL_HOST $SQL_HOST"
echo "SQL_PORT $SQL_PORT"
echo "DATABASE $DATABASE"
echo "########################################"
echo "#     END CHECK                        #"
echo "########################################"

# MIGRATE ANY CHANGES TO THE DATABASE BUT REMOVE IT FIRST.
python manage.py flush --no-input
python manage.py migrate

# Let the container keep his job
exec "$@"