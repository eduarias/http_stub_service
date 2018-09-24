FROM python:3.6-alpine

RUN mkdir apps
COPY requirements.txt apps/
RUN apk add --update \
    build-base \
    gfortran \
    python \
    python-dev \
    py-pip
RUN pip install -r apps/requirements.txt

COPY stub_server.py apps/
COPY config.py apps/

WORKDIR apps/

CMD ["/usr/local/bin/gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "stub_server:app"]