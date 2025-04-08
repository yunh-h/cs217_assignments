FROM python:3.12-slim

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt
EXPOSE 8080
ENV FLASK_APP=run.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
