FROM python:3.9.1-slim

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y curl && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY todo-backend.py .

RUN pip install flask requests psycopg2-binary

CMD ["python", "todo-backend.py"]
