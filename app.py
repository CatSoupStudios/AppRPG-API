from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/tienda', methods=['GET'])
def obtener_items_tienda():
    with open('tienda.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

