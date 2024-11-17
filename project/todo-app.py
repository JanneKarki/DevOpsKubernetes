from flask import Flask, send_file
import os
import requests
from datetime import datetime, timedelta

app = Flask(__name__)
image_path = "/usr/src/app/files/hourly_image.jpg"
update_interval = timedelta(hours=1)

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

@app.route('/todo')
def home():
    check_image_update()
    return f"""
            <html>
                <head>
                    <title>Todo-App-Server</title>
                </head>
                <body>
                    <h1>Hello</h1>
                    <img src="/todo/image" alt="Random Image">
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
