from python:2-alpine

COPY . /usr/app

COPY requirements.txt /tmp/requirements.txt
RUN cd /tmp && pip install -r requirements.txt

WORKDIR /usr/app

CMD ["gunicorn", "server:app", "-b", "0.0.0.0:8000"]