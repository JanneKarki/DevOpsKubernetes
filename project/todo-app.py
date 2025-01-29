from flask import Flask, send_file, request
import os
import requests
from datetime import datetime, timedelta
import logging

app = Flask(__name__)
image_path = "/usr/src/app/files/hourly_image.jpg"
update_interval = timedelta(hours=1)
backend_service_url = os.getenv("BACKEND_SERVICE_URL")
logging.basicConfig(level=logging.INFO)

def download_image():
    response = requests.get("https://picsum.photos/1200")
    with open(image_path, "wb") as file:
        file.write(response.content)
    logging.info("Image downloaded successfully")

def check_image_update():
    if os.path.exists(image_path):
        last_modified_time = datetime.fromtimestamp(os.path.getmtime(image_path))
        if datetime.now() - last_modified_time >= update_interval:
            download_image()
    else:
        download_image()

@app.route('/', methods=['GET'])
def home():
    return "Todo App running!!", 200

@app.route('/todo', methods=['GET', 'POST'])
def todo():
    if request.method == 'POST':
        new_todo = request.form.get('todo')
        if new_todo:
            response = requests.post(backend_service_url, json={"todo": new_todo})
            if response.status_code == 201:
                logging.info("Todo successfully sent to backend: %s", new_todo)
            else:
                logging.error("Failed to create todo: %s | Backend response: %s", new_todo, response.json())
                
    response = requests.get(backend_service_url)
    todos = response.json()
    
    check_image_update()
    todo_list_html = ''.join(f"<li>{todo}</li>" for todo in todos)
    
    return f"""
            <html>
                <head>
                    <title>Todo-App-Server</title>
                </head>
                <body>
                    <h1>Todo App</h1>
                    <img src="/todo/image" alt="Random Image">
                    <form method="POST">
                        <input type="text" name="todo">
                        <button type="submit">Create TODO</button>
                    </form>
                    <ul>
                        {todo_list_html}
                    </ul>
                </body>
            </html>
            """

@app.route('/todo/image')
def serve_image():
    check_image_update()
    return send_file(image_path, mimetype='image/jpeg')

if __name__ == '__main__':
    port = int(os.getenv("PORT", 8081))
    app.run(host='0.0.0.0', port=port)
