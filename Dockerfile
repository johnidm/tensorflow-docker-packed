FROM python:3.8.6-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app app

CMD ["python", "-u", "/app/app/app.py"]
