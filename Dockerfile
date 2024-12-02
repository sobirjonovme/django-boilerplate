FROM python:3.12.2-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV CRYPTOGRAPHY_DONT_BUILD_RUST 1

# Install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc netcat-traditional gettext

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
COPY entrypoints/ $APP_HOME/entrypoints/

# copy project
COPY . $APP_HOME

# chmod all entrypoints files recursively
RUN ["chmod", "+x", "-R", "/home/app/web/entrypoints/"]
