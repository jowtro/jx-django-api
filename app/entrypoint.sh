#!/bin/bash
set -e

echo "########################################"
echo "#      CHECK IF POSTGRESQL IS UP       #"
echo "########################################"
echo "Waiting PostgreSQL"
python check-pgsql.py
echo "finished ..."

python manage.py flush --no-input
python manage.py migrate

# Let the container keep his job
exec "$@"