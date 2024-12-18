from flask import Flask, jsonify
import hashlib
import uuid
import requests
import os

app = Flask(__name__)
timestamp_path = "/usr/src/app/files/timestamp.txt"
pingpong_service_url = "http://pingpong-svc:8080/pingpong"  
information = "/usr/src/app/config/information.txt"

random_string = str(uuid.uuid4())

@app.route('/', methods=['GET'])
def get_status():
    try:
        with open(timestamp_path, "r") as timestamp_file:
            timestamp = timestamp_file.read()

        response = requests.get(pingpong_service_url)
        response.raise_for_status()
        ping_count = response.text.strip()


        with open(information, "r") as information_file:
            file_content = information_file.read().strip()
        
        message = os.getenv("MESSAGE", "MESSAGE not set")

        hash_value = hashlib.sha256(random_string.encode()).hexdigest()
        
        return f"""
                file content: {file_content}
                env variable: MESSAGE={message}
                {timestamp}: {hash_value}.
                Ping / Pongs: {ping_count}
                """

    except FileNotFoundError:
        return jsonify({"error": "No timestamp file found"}), 404
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Error connecting to pingpong service: {e}"}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
