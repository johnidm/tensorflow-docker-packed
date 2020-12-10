FROM python:3.8.6-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt --use-feature=2020-resolver

COPY app app

CMD ["python", "-u", "/app/app/main.py"]
