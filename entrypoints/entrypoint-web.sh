#!/bin/sh

# Wait for the database to be ready
echo "Waiting for DB to be ready... $DB_HOST:$DB_PORT"
while ! nc -z $DB_HOST $DB_PORT; do
  sleep 1
  echo "Waiting for DB... $DB_HOST:$DB_PORT"
done
echo "DB is ready."

python manage.py migrate
python manage.py collectstatic --noinput

exec "$@"
