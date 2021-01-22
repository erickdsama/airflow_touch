FROM python:3.7

RUN adduser  linkauser
ADD . /flask
WORKDIR /flask
RUN pip install -r requirements.txt
RUN pip install gunicorn

RUN ["chmod", "a+x", "boot.sh"]

ENV FLASK_DEBUG 1
ENV FLASK_APP main.py
USER linkauser

ENTRYPOINT ["./boot.sh"]
