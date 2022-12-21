FROM python:3.9
ENV PYTHONUNBUFFERED=1

RUN \
  apt-get -y update && \
  apt-get install -y gettext && \
  apt-get clean

ENV WEBAPP_DIR=/code

RUN mkdir $WEBAPP_DIR

WORKDIR $WEBAPP_DIR

COPY requirements.txt $WEBAPP_DIR/

RUN pip install -r requirements.txt

ADD . $WEBAPP_DIR/
