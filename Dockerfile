from python:3.9

WORKDIR /bot

COPY config.yaml .
COPY requirements.txt .
COPY main.py .
COPY app .

RUN pip install -r requirements.txt