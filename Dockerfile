FROM python:3.9.2-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV CRYPTOGRAPHY_DONT_BUILD_RUST 1

# install psycopg2 dependencies
RUN apk update \
    && apk add libffi-dev postgresql-dev wkhtmltopdf gcc python3-dev musl-dev py-pip jpeg-dev zlib-dev \
    && apk add libressl-dev perl rust libmagic pango openjpeg-dev g++

RUN apk --no-cache add \
    icu-dev \
    gettext \
    gettext-dev


RUN apk upgrade -U \
    && apk add ca-certificates ffmpeg libva-intel-driver \
    && rm -rf /var/cache/*

RUN apk --no-cache add glib-dev poppler-glib vips-dev vips-tools poppler-utils

RUN mkdir -p /home/app
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
RUN mkdir $APP_HOME/media
RUN mkdir $APP_HOME/locale
WORKDIR $APP_HOME

COPY requirements/ .

RUN pip install --upgrade pip
RUN pip install -r production.txt

# copy entrypoint.sh
COPY ./entrypoint.sh $APP_HOME

# copy project
COPY . $APP_HOME

# run entrypoint.prod.sh
RUN ["chmod", "+x", "/home/app/web/entrypoint.sh"]
ENTRYPOINT ["/home/app/web/entrypoint.sh"]
