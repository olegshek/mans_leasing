FROM ubuntu:18.04

RUN set -ex \
    \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        ca-certificates curl netbase wget \
        git openssh-client \
        libcurl4-openssl-dev libpq-dev libjpeg-dev libpng-dev libsqlite3-dev libxml2-dev libyaml-dev \
        libtool libssl-dev build-essential \
        python3 python3-dev python3-virtualenv python3-cffi python3-pip libcairo2 \
        libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev \
        shared-mime-info

ENV VIRTUAL_ENV /app/venv

RUN python3 -m virtualenv --python=/usr/bin/python3 $VIRTUAL_ENV

ENV PATH $VIRTUAL_ENV/bin:$PATH

COPY ./requirements.txt /app/

RUN pip install --upgrade pip && pip install -r /app/requirements.txt

COPY . /app/

WORKDIR /app

COPY ./docker/mans_leasing/gunicorn.conf.py /app/gunicorn.conf.py

EXPOSE 8000

CMD gunicorn -c /app/gunicorn.conf.py --log-level=${DJANGO_LOGLEVEL} --name ${SERVICE_VARIANT} --max-requests=1000 --access-logfile - --error-logfile - --bind=0.0.0.0:8000 config.${WSGI_NAME}:application

