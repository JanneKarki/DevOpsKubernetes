FROM python:3.9.1-slim

WORKDIR /usr/src/app

COPY todo-backend.py .

RUN pip install flask requests psycopg2-binary

CMD ["python", "todo-backend.py"]
