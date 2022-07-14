from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():
    return "Test"

@app.route('/cloneTest')
def clonepage():
    return "clone Test"

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

