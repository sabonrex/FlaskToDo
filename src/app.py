from flask import Flask, jsonify, request
import json
app = Flask(__name__)



todos = [{"label": "My first task", "done": True}]


@app.route('/hello', methods=['GET'])
def hello_world():
    return 'Hello, World!'


@app.route('/todos', methods=['GET'])
def all_todo():
    return jsonify(todos), 200


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json()
    todos.append(request_body)
    print("Incoming request with the following body", request_body)
    return jsonify(todos), 200


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ", position)
    todos.pop(position)
    return jsonify(todos), 200



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)