FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt

COPY src/ .

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]

