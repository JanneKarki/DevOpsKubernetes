from flask import Flask
import os

app = Flask(__name__)
file_path = "/usr/src/app/files/pingpong.txt"
counter = 0

@app.route('/pingpong', methods=['GET'])
def ping_pong():
    global counter
    response = f"{counter}\n"
    with open(file_path, "w") as file:
        file.write(response)
    counter += 1
    return response

if __name__ == '__main__':
    port = int(os.getenv("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
