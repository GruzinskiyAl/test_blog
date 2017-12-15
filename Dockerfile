FROM python:3
ENV PYTHONUNBUFFERED 1
ADD . /test_project
WORKDIR /test_project
RUN pip install -r requirements.txt
