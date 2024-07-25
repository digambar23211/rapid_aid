from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello'})

if __name__ == '__main__':
    app.run(debug=True)
