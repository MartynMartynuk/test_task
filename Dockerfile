# pull official base image
FROM python:3.10.3

#SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

WORKDIR /test_task

# copy project
COPY . .
RUN pip install -r requirements.txt