from flask import Flask, jsonify
import hashlib
import uuid

app = Flask(__name__)
file_path = "/usr/src/app/files/timestamp.txt"

random_string = str(uuid.uuid4())

@app.route('/', methods=['GET'])
def get_status():
    try:
        with open(file_path, "r") as file:
            timestamp = file.read()
        hash_value = hashlib.sha256(random_string.encode()).hexdigest()
        return jsonify({
            "timestamp": timestamp,
            "hash": hash_value
        })
    except FileNotFoundError:
        return jsonify({"error": "No timestamp file found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
