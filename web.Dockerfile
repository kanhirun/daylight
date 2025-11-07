FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY web/requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY web/ .

EXPOSE 8000
