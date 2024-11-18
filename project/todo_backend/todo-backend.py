from flask import Flask, request, jsonify

app = Flask(__name__)
todos = ["TODO 1", "TODO 2"]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def create_todo():
    new_todo = request.json.get('todo')
    if new_todo:
        todos.append(new_todo)
        return jsonify({"message": "Todo added successfully"}), 201
    return jsonify({"error": "Invalid todo"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
