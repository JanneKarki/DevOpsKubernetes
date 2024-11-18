FROM python:3.9-slim

WORKDIR /usr/src/app

COPY todo-backend.py .

RUN pip install flask requests

CMD ["python", "todo-backend.py"]
