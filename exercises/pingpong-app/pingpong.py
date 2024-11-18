from flask import Flask
import os

app = Flask(__name__)

counter = 0

@app.route('/pingpong', methods=['GET'])
def ping_pong():
    global counter
    response = f"{counter}\n"
    counter += 1
    return response

if __name__ == '__main__':
    port = int(os.getenv("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
