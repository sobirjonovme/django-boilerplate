#!/bin/sh

until python manage.py migrate
do
    echo "Waiting for db to be ready..."
    sleep 0.5
done

python manage.py collectstatic --noinput

exec "$@"
