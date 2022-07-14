from flask import Flask, jsonify, request
from datetime import datetime
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

@app.route('/')
def homepage():
    return "Test"

@app.route('/cloneTest')
def clonepage():
    return "clone Test"

@app.route('/getName', methods=['GET'])
def getName():
    name = {"name": "Nishant Gada"}
    result = jsonify(name)
    return result
    

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

