from python:3.9

WORKDIR /app

COPY requirements.txt .
COPY main.py .

RUN pip install -r requirements.txt