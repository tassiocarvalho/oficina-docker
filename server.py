from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulando uma base de dados em memória com uma lista
data = []

@app.route('/items', methods=['POST'])
def create():
    item = request.json
    data.append(item)
    return jsonify(item), 201

@app.route('/items', methods=['GET'])
def read():
    return jsonify(data), 200

@app.route('/items/<int:item_id>', methods=['PUT'])
def update(item_id):
    if item_id >= len(data) or item_id < 0:
        return jsonify({"error": "Item not found"}), 404
    
    item = request.json
    data[item_id] = item
    return jsonify(item), 200

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete(item_id):
    if item_id >= len(data) or item_id < 0:
        return jsonify({"error": "Item not found"}), 404
    
    deleted_item = data.pop(item_id)
    return jsonify(deleted_item), 200

if __name__ == '__main__':
    app.run(debug=True)
