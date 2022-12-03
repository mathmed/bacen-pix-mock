FROM python:3.10

ADD requirements.dev.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 80

WORKDIR /home/app

CMD [ "uvicorn", "app.main:app", "--host=0.0.0.0", "--port=80", "--reload" ]
