FROM python:3.9-slim

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

WORKDIR /app

RUN mkdir data

COPY . .

ENTRYPOINT ["python", "collect.py"]
