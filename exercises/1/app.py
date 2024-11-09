from flask import Flask, jsonify
import time
import uuid
from datetime import datetime
import threading

app = Flask(__name__)


random_string = str(uuid.uuid4())
current_time = datetime.now().isoformat()

def update_timestamp():
    global current_time
    while True:
        current_time = datetime.now().isoformat()
        print(f"{current_time}: {random_string}", flush=True)
        time.sleep(5)

thread = threading.Thread(target=update_timestamp, daemon=True)
thread.start()


@app.route('/', methods=['GET'])
def get_status():
    return jsonify({
        "timestamp": current_time,
        "random_string": random_string
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
