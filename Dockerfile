FROM python:3.8.5-buster

ENV PYTHON_ENVIROMENT='dev'

RUN mkdir /app

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt
RUN pip install gunicorn

EXPOSE 8000

CMD ["gunicorn", "--config", "gunicorn.py", "wsgi:app"]