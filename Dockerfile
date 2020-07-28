FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir  /src/ /src/app/
WORKDIR /src/app/
COPY requirements.txt /src/app/
RUN  pip install -r requirements.txt
RUN pip install -Iv Django==3.0.4

COPY . /src/app/
