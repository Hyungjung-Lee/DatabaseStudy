from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/')
@app.route('/get', methods=['GET'])
def get():
    return 'Hello, World! GET'
@app.route('/post', methods=['POST'])
def post():
    data = request.json
    return jsonify(data)
@app.route('/put', methods=['PUT'])
def put():
    return 'Hello, World! PUT'
@app.route('/delete', methods=['DELETE'])
def delete():
    return 'Hello, World! DELETE'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)