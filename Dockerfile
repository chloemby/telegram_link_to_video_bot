from alpine:3.9

WORKDIR /app

COPY requirements.txt .
COPY main.py .

RUN pip insttall -r requirements.txt