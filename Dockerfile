FROM python:3.10.3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

WORKDIR /test_task

COPY . .
RUN pip install -r requirements.txt