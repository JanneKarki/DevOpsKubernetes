from flask import Flask, jsonify
import hashlib
import uuid

app = Flask(__name__)
timestamp_path = "/usr/src/app/files/timestamp.txt"
pingpong_path = "/usr/src/app/files/pingpong.txt"

random_string = str(uuid.uuid4())

@app.route('/', methods=['GET'])
def get_status():
    try:
        with open(timestamp_path, "r") as timestamp_file:
            timestamp = timestamp_file.read()
        with open(pingpong_path, "r") as pingpong_file:
            ping_count = pingpong_file.read()

        hash_value = hashlib.sha256(random_string.encode()).hexdigest()
        return f"{timestamp}: {hash_value}. \nPing / Pongs : {ping_count}"

    except FileNotFoundError:
        return jsonify({"error": "No timestamp file found"}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
