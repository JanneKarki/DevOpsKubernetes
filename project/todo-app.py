from flask import Flask, send_file, request
import os
import requests
from datetime import datetime, timedelta

app = Flask(__name__)
image_path = "/usr/src/app/files/hourly_image.jpg"
update_interval = timedelta(hours=1)
todos = ["TODO 1", "TODO 2"]

def download_image():
    response = requests.get("https://picsum.photos/1200")
    with open(image_path, "wb") as file:
        file.write(response.content)

def check_image_update():
    if os.path.exists(image_path):
        last_modified_time = datetime.fromtimestamp(os.path.getmtime(image_path))
        if datetime.now() - last_modified_time >= update_interval:
            download_image()
    else:
        download_image()

@app.route('/todo', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        new_todo = request.form.get('todo')
        if new_todo:
            todos.append(new_todo)
    
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
                        <input type="text" name="todo" maxlength="140">
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
