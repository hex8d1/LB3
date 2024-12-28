from flask import Flask, request, jsonify, abort
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {"admin": "password123"}
catalog = {}

@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username
    return None

@app.route('/items', methods=['GET', 'POST'])
@auth.login_required
def items():
    if request.method == 'GET':
        return jsonify(catalog)
    elif request.method == 'POST':
        data = request.json
        if not data or 'id' not in data:
            abort(400, "Invalid data. 'id' is required.")
        if data['id'] in catalog:
            abort(400, "Item with this ID already exists.")
        catalog[data['id']] = data
        return jsonify({"message": "Item added successfully", "item": data}), 201

@app.route('/items/<int:item_id>', methods=['GET', 'PUT', 'DELETE'])
@auth.login_required
def item(item_id):
    if item_id not in catalog:
        abort(404, "Item not found.")
    if request.method == 'GET':
        return jsonify(catalog[item_id])
    elif request.method == 'PUT':
        data = request.json
        if not data:
            abort(400, "Invalid data.")
        catalog[item_id].update(data)
        return jsonify({"message": "Item updated successfully", "item": catalog[item_id]})
    elif request.method == 'DELETE':
        del catalog[item_id]
        return jsonify({"message": "Item deleted successfully"})

if __name__ == "__main__":
    app.run(port=8000)
