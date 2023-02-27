# pull official base image
FROM python:3.10.3-alpine

SHELL ["/bin/basg", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

WORKDIR /test_task

# copy project
COPY . .
RUN pip install -r requirements.txt