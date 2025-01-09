FROM python:3.9.1-slim

WORKDIR /usr/src/app

COPY todo-app.py .

RUN pip install flask requests

CMD ["python", "todo-app.py"]
