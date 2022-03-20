FROM python:3.8-slim-buster

# create directory for the app user
RUN mkdir -p /home/app

# create the app user
RUN addgroup --system app && adduser --system --group app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/code
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# set environment variables
ENV PYTHONHONDONTWRITTEBYTECODE 1
ENV PYTHONBUFFERED 1
ENV ENVIRONMENT prod

# Install System Dependencies
RUN apt-get update \
    && apt-get -y install netcat gcc libpq-dev \
    && apt-get clean 

# Install Python Dependencies
RUN pip install --upgrade pip
RUN pip install -U setuptools
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy app
COPY . .

RUN chown -R app:app $APP_HOME

# change to the app user
USER app

# Run Gunicorn
CMD gunicorn --bind 0.0.0.0:5000 main:app -k uvicorn.workers.UvicornWorker
