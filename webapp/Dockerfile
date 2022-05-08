FROM python:3.8.10

WORKDIR /webapp
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . .
ENTRYPOINT flask run --host=0.0.0.0

