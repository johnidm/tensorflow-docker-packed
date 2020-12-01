FROM python:3.8.6-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY myapp myapp

CMD ["python", "-u", "/app/myapp/app.py"]
