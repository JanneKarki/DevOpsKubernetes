from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Server started in port " + os.getenv("PORT", "5000")

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
