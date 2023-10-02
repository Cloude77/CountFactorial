
FROM python:3.11

WORKDIR /app

COPY . /app


ENV PYTHONPATH=/app


CMD [ "python", "-u", "factorial.py" ]
